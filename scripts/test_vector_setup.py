from pathlib import Path
import json
import chromadb

# Check JSON chunk file
json_path = Path("data/clean_chunks.json")

with open(json_path, "r", encoding="utf-8") as f:
    chunks = json.load(f)

print(f"Successfully loaded {len(chunks)} chunks from JSON.\n")
print("Example chunk:")
print(chunks[0])

# Check Chroma import and client
print("\nChroma imported successfully.")

client = chromadb.PersistentClient(path="chroma_db")
print("Connected to persistent Chroma database.")

# Check collection
collection = client.get_collection(name="policy_chunks")
print("Loaded collection: policy_chunks")

# Check number of stored records
count = collection.count()
print(f"Collection contains {count} records.")

if count > 0:
    print("Vector setup looks healthy.")
else:
    print("Warning: collection exists but contains no records.")
