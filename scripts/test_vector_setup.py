from pathlib import Path
import json

json_path = Path("data/clean_chunks.json")

with open(json_path, "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Successfully loaded {len(chunks)} chunks from JSON.\n")
print("Example chunk:")
print(chunks[0])

import chromadb
print("\nChroma imported successfully.")
