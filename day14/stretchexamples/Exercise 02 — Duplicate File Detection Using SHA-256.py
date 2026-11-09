'''
Exercise 02 — Duplicate File Detection Using SHA-256
'''

from collections import defaultdict
from hashlib import sha256
from pathlib import Path


def file_hash(path):
    digest = sha256()

    with path.open("rb") as file:
        while chunk := file.read(65536):
            digest.update(chunk)

    return digest.hexdigest()


folder = Path("duplicate_test")
folder.mkdir(exist_ok=True)

(folder / "a.txt").write_text("Python")
(folder / "b.txt").write_text("Python")
(folder / "c.txt").write_text("Java")

groups = defaultdict(list)

for path in folder.iterdir():
    if path.is_file():
        groups[file_hash(path)].append(path.name)

for digest, filenames in groups.items():
    if len(filenames) > 1:
        print("Duplicate group:", filenames)
        print("SHA-256:", digest)