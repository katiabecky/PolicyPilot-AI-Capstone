from pathlib import Path

policy_folder = Path("data/policies")
policy_files = list(policy_folder.glob("*.md"))

documents = []

for f in policy_files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    document = {
        "filename": f.name,
        "content": content
    }

    documents.append(document)

print(f"Loaded {len(documents)} documents.\n")

for doc in documents:
    print("=" * 50)
    print(f"Filename: {doc['filename']}")
    print(f"Character count: {len(doc['content'])}")
    print("Preview:")
    print(doc["content"][:300])
    print("\n")
