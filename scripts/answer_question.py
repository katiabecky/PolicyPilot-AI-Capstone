import chromadb


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

    # Penalize generic/header chunks
    if is_generic_chunk(doc, meta):
        score -= 3

    # Reward section-title matches
    important_terms = q.replace("?", "").split()
    for term in important_terms:
        if term in section:
            score += 2
        if term in text:
            score += 1

    # Heuristic boost for vacation allowance vs carryover
    if "vacation" in q and "days" in q:
        if "annual vacation allowance" in section:
            score += 5
        if "carryover" in section:
            score -= 2

    # Heuristic boost for password requirement questions
    if "password" in q:
        if "password requirements" in section:
            score += 5

    # Heuristic boost for expense submission questions
    if "expense" in q or "reimbursement" in q:
        if "submission process" in section:
            score += 5

    # Heuristic boost for harassment/reporting questions
    if "harassment" in q or "suspect harassment" in q:
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

    # If all scores are weak, refuse
    if max(scores) < 2:
        return True

    # If most results are generic headers, refuse
    generic_count = sum(is_generic_chunk(d, m) for d, m in zip(docs, metas))
    if generic_count >= 2:
        return True

    return False


def get_best_result(query, results):
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    ids = results["ids"][0]

    scored = []
    for doc, meta, chunk_id in zip(docs, metas, ids):
        scored.append((score_chunk(query, doc, meta), doc, meta, chunk_id))

    scored.sort(key=lambda x: x[0], reverse=True)
    return scored


def build_direct_answer(query, best_doc, best_meta):
    section = best_meta.get("section_title", "Unknown section")
    filename = best_meta.get("filename", "Unknown source")

    answer = f"Based on {filename} ({section}), here is the most relevant information:\n\n{best_doc}"
    return answer


def print_sources(scored_results):
    print("\nSources:\n")
    for i, (_, doc, meta, chunk_id) in enumerate(scored_results[:3], start=1):
        print(f"{i}. Source: {meta['filename']} | Section: {meta['section_title']}")
        print(f"   Chunk ID: {chunk_id}")
        print()


def answer_question(query, n_results=3):
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_collection(name="policy_chunks")

    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    print("\n" + "=" * 70)
    print(f"QUESTION: {query}")
    print("=" * 70)

    if is_out_of_scope(query, results):
        print("\nAnswer:\n")
        print("I could not find enough support in the current policy documents to answer that question.")
        print("\nTry asking about company policies such as vacation, expenses, remote work, conduct, or IT security.\n")
        return

    scored_results = get_best_result(query, results)
    best_score, best_doc, best_meta, best_chunk_id = scored_results[0]

    answer = build_direct_answer(query, best_doc, best_meta)

    print("\nAnswer:\n")
    print(answer)

    print_sources(scored_results)


if __name__ == "__main__":
    print("PolicyPilot AI - Policy Q&A")
    print("Type your question below.")
    print("Type 'exit' to quit.\n")

    while True:
        user_question = input("Enter your policy question: ").strip()

        if user_question.lower() == "exit":
            print("Goodbye.")
            break

        if not user_question:
            print("Please enter a question.\n")
            continue

        answer_question(user_question)
