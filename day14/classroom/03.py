'''
Example 03 — File Modes and Cursor Position
'''
from pathlib import Path

path = Path("file_modes.txt")

with path.open("w+", encoding="utf-8") as file:
    file.write("Python Deep Dive")

    print("Cursor after write:", file.tell())

    file.seek(0)

    print("Content:", file.read())

with path.open("a+", encoding="utf-8") as file:
    file.write("\nDay 14")

    file.seek(0)

    print(file.read())

try:
    with path.open("x", encoding="utf-8") as file:
        file.write("New file")

except FileExistsError:
    print("File already exists")