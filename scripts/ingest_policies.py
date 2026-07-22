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

chunks = []

for doc in documents:
    parts = doc["content"].split("## ")

    for part in parts:
        part = part.strip()

        if not part:
            continue

        lines = part.splitlines()
        section_title = lines[0].strip()
        section_content = "\n".join(lines[1:]).strip()

        chunk = {
            "filename": doc["filename"],
            "section_title": section_title,
            "content": section_content
        }

        chunks.append(chunk)

print(f"Loaded {len(documents)} documents.")
print(f"Created {len(chunks)} chunks.\n")

for chunk in chunks[:10]:
    print("=" * 50)
    print(f"Filename: {chunk['filename']}")
    print(f"Section: {chunk['section_title']}")
    print(f"Character count: {len(chunk['content'])}")
    print("Preview:")
    print(chunk["content"][:300])
    print("\n")
