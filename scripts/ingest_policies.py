from pathlib import Path

policy_folder = Path("data/policies")
policy_files = list(policy_folder.glob("*.md"))

print("Found policy files:")
for f in policy_files:
    print("-", f.name)

print("\nReading file contents...\n")

for f in policy_files:
    print("=" * 50)
    print(f"FILE: {f.name}")

    with open(f, "r", encoding="utf-8") as file:
        content = file.read()

    print("Preview:")
    print(content[:500])
    print("\n")
