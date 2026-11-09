'''
Example 02 — Writing, Reading and Appending Text Files
'''

from pathlib import Path

path = Path("students.txt")

path.write_text(
    "Alice,90\nBob,85\n",
    encoding="utf-8"
)

print(path.read_text(encoding="utf-8"))

with path.open("a", encoding="utf-8") as file:
    file.write("Charlie,95\n")

with path.open("r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())