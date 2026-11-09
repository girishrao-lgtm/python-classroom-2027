'''
Exercise 01 — Recursive Directory Inventory
'''

from pathlib import Path

root = Path("sample_project")

(root / "src").mkdir(parents=True, exist_ok=True)
(root / "docs").mkdir(parents=True, exist_ok=True)

(root / "src" / "main.py").write_text("print('Hello')")
(root / "src" / "utils.py").write_text("x = 10")
(root / "docs" / "readme.txt").write_text("Documentation")

files = []

for path in root.rglob("*"):
    if path.is_file():
        files.append({
            "path": str(path.relative_to(root)),
            "extension": path.suffix,
            "size": path.stat().st_size
        })

for file in sorted(files, key=lambda item: item["path"]):
    print(file)

print("Total files:", len(files))
print("Total bytes:", sum(file["size"] for file in files))