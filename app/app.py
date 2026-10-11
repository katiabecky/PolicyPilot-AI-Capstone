import json
from pathlib import Path

import chromadb
import streamlit as st
from chromadb.errors import NotFoundError


BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "chroma_db"
CHUNKS_FILE = BASE_DIR / "data" / "clean_chunks.json"
COLLECTION_NAME = "policy_chunks"


# -----------------------------
# Collection setup
# -----------------------------
def load_chunks_from_json():
    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_or_create_policy_collection():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    try:
        collection = client.get_collection(name=COLLECTION_NAME)
        if collection.count() > 0:
            return collection
    except NotFoundError:
        collection = client.create_collection(name=COLLECTION_NAME)
    else:
        # Collection exists but is empty; refill it.
        pass

    chunks = load_chunks_from_json()

    ids = [chunk["chunk_id"] for chunk in chunks]
    documents = [chunk["content"] for chunk in chunks]
    metadatas = [
        {
            "filename": chunk.get("filename", ""),
            "section_title": chunk.get("section_title", "")
        }
        for chunk in chunks
    ]

    if collection.count() == 0:
        collection.add(ids=ids, documents=documents, metadatas=metadatas)

    return collection


# -----------------------------
# Helper functions
# -----------------------------
def is_generic_chunk(doc, meta):
    section = meta.get("section_title", "").strip().lower()
    content = doc.strip().lower()

    if section.startswith("#"):
        return True
    if "effective date" in content and "version:" in content:
        return True
    return False


def question_needs_specific_secret(query):
    q = query.lower()
    secret_keywords = [
        "password today",
        "wifi password",
        "wi-fi password",
        "ceo assistant",
        "stock price",
        "today's password",
        "current password"
    ]
    return any(term in q for term in secret_keywords)


def score_chunk(query, doc, meta):
    q = query.lower()
    text = doc.lower()
    section = meta.get("section_title", "").lower()

    score = 0

    if is_generic_chunk(doc, meta):
        score -= 3

    important_terms = q.replace("?", "").split()
    for term in important_terms:
        if term in section:
            score += 2
        if term in text:
            score += 1

    if "vacation" in q and "days" in q:
        if "annual vacation allowance" in section:
            score += 5
        if "carryover" in section:
            score -= 2

    if "password" in q:
        if "password requirements" in section:
            score += 5

    if "expense" in q or "reimbursement" in q:
        if "submission process" in section:
            score += 5

    if "harassment" in q:
        if "anti-harassment" in section or "reporting concerns" in section:
            score += 4

    return score


def is_out_of_scope(query, results):
    docs = results["documents"][0]
    metas = results["metadatas"][0]

    if not docs:
        return True

    if question_needs_specific_secret(query):
        return True

    scores = [score_chunk(query, d, m) for d, m in zip(docs, metas)]

    if max(scores) < 2:
        return True

    generic_count = sum(is_generic_chunk(d, m) for d, m in zip(docs, metas))
    if generic_count >= 2:
        return True

    return False


def get_best_results(query, results):
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    ids = results["ids"][0]

    scored = []
    for doc, meta, chunk_id in zip(docs, metas, ids):
        scored.append((score_chunk(query, doc, meta), doc, meta, chunk_id))

    scored.sort(key=lambda x: x[0], reverse=True)
    return scored


def build_direct_answer(best_doc, best_meta):
    section = best_meta.get("section_title", "Unknown section")
    filename = best_meta.get("filename", "Unknown source")

    return (
        f"Based on **{filename}** ({section}), here is the most relevant information:\n\n"
        f"{best_doc}"
    )


def answer_question(query, n_results=3):
    collection = get_or_create_policy_collection()

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    if is_out_of_scope(query, results):
        return {
            "supported": False,
            "answer": "I could not find enough support in the current policy documents to answer that question.",
            "sources": []
        }

    scored_results = get_best_results(query, results)
    best_score, best_doc, best_meta, best_chunk_id = scored_results[0]

    return {
        "supported": True,
        "answer": build_direct_answer(best_doc, best_meta),
        "sources": scored_results[:3]
    }


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="PolicyPilot AI", page_icon="📘", layout="centered")

st.title("📘 PolicyPilot AI")
st.subheader("Retrieval-Augmented Policy Assistant")
st.write(
    "Ask a question about company policies. The assistant will return the most relevant policy-backed answer it can support."
)

question = st.text_input(
    "Enter your policy question:",
    placeholder="Example: What are the password requirements?"
)

if st.button("Ask PolicyPilot"):
    if not question.strip():
        st.warning("Please enter a question before submitting.")
    else:
        try:
            with st.spinner("Searching policy documents..."):
                result = answer_question(question)

            st.markdown("## Answer")
            if result["supported"]:
                st.success(result["answer"])

                st.markdown("## Sources")
                for i, (_, doc, meta, chunk_id) in enumerate(result["sources"], start=1):
                    st.markdown(
                        f"**{i}. {meta['filename']}** — {meta['section_title']}  \n"
                        f"`Chunk ID: {chunk_id}`"
                    )
                    with st.expander(f"View source excerpt {i}"):
                        st.write(doc)
            else:
                st.error(result["answer"])
                st.info("Try asking about company policies such as vacation, expenses, remote work, conduct, or IT security.")
        except Exception as e:
            st.error(f"The app ran into an error while searching the policy database: {e}")
            st.info("If this is the first run after deployment, try refreshing once after a few seconds while the policy collection initializes.")
