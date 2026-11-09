'''
Example 16 — File Handling with with
'''

from pathlib import Path

path = Path("students.txt")

with path.open("w", encoding="utf-8") as file:
    file.write("Alice,90\n")
    file.write("Bob,85\n")
    file.write("Charlie,95\n")


with path.open("r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())