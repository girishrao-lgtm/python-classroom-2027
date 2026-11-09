'''
Example 13 — Temporary Files and Directories
'''
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "temporary.txt"

    path.write_text(
        "Temporary processing data",
        encoding="utf-8"
    )

    print("Exists inside:", path.exists())
    print(path.read_text(encoding="utf-8"))

print("Exists after cleanup:", path.exists())

with tempfile.TemporaryFile(mode="w+t", encoding="utf-8") as file:
    file.write("Temporary content")
    file.seek(0)

    print(file.read())