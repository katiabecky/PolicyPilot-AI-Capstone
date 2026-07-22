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

raw_chunks = []

for doc in documents:
    parts = doc["content"].split("## ")

    for part in parts:
        part = part.strip()

        if not part:
            continue

        lines = part.splitlines()
        section_title = lines[0].strip()
        section_content = "\n".join(lines[1:]).strip()

        raw_chunk = {
            "filename": doc["filename"],
            "section_title": section_title,
            "content": section_content
        }

        raw_chunks.append(raw_chunk)

clean_chunks = []

for i, chunk in enumerate(raw_chunks, start=1):
    cleaned_content = " ".join(chunk["content"].split())

    clean_chunk = {
        "chunk_id": f"{Path(chunk['filename']).stem}_{i}",
        "filename": chunk["filename"],
        "section_title": chunk["section_title"],
        "content": cleaned_content
    }

    clean_chunks.append(clean_chunk)

print(f"Loaded {len(documents)} documents.")
print(f"Created {len(raw_chunks)} raw chunks.")
print(f"Created {len(clean_chunks)} cleaned chunks.\n")

for chunk in clean_chunks[:10]:
    print("=" * 50)
    print(f"Chunk ID: {chunk['chunk_id']}")
    print(f"Filename: {chunk['filename']}")
    print(f"Section: {chunk['section_title']}")
    print(f"Character count: {len(chunk['content'])}")
    print("Preview:")
    print(chunk["content"][:300])
    print("\n")
