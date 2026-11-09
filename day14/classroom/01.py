'''
Example 01 — Path Creation and Inspection Using pathlib
'''
from pathlib import Path

current = Path.cwd()

print("Current directory:", current)
print("Home directory:", Path.home())

path = Path("day14_data") / "students.txt"

print("File name:", path.name)
print("Stem:", path.stem)
print("Suffix:", path.suffix)
print("Parent:", path.parent)
print("Absolute path:", path.resolve())

path.parent.mkdir(parents=True, exist_ok=True)

print("Directory exists:", path.parent.exists())
print("Is directory:", path.parent.is_dir())