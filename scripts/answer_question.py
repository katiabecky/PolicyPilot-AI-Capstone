import chromadb

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

    retrieved_docs = results["documents"][0]
    retrieved_meta = results["metadatas"][0]
    retrieved_ids = results["ids"][0]

    print("\nSuggested Answer:\n")
    print("Based on the policy documents, here is the most relevant information:\n")

    for i in range(len(retrieved_docs)):
        print(f"{i+1}. Source: {retrieved_meta[i]['filename']} | Section: {retrieved_meta[i]['section_title']}")
        print(f"   Chunk ID: {retrieved_ids[i]}")
        print(f"   Content: {retrieved_docs[i]}")
        print()


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
