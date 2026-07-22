import chromadb

# Connect to the existing persistent Chroma database
client = chromadb.PersistentClient(path="chroma_db")

# Load the existing collection
collection = client.get_collection(name="policy_chunks")

# Test queries
queries = [
    "How many vacation days do employees get?",
    "Can employees work remotely full time?",
    "What should I do if I suspect harassment?",
    "How do I submit an expense reimbursement?",
    "What are the password requirements?"
]

for query in queries:
    print("\n" + "=" * 70)
    print(f"QUERY: {query}\n")

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    for i in range(len(results["ids"][0])):
        print("-" * 60)
        print(f"Result {i+1}")
        print(f"Chunk ID: {results['ids'][0][i]}")
        print(f"Filename: {results['metadatas'][0][i]['filename']}")
        print(f"Section title: {results['metadatas'][0][i]['section_title']}")
        print(f"Preview: {results['documents'][0][i][:300]}")
        print()
