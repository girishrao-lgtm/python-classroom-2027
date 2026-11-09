'''
Example 10 — JSON Serialization and Deserialization
'''

import json
from pathlib import Path

student = {
    "roll_number": 101,
    "name": "Alice",
    "marks": [90, 85, 95],
    "active": True,
    "department": "AI Engineering"
}

path = Path("student.json")

with path.open("w", encoding="utf-8") as file:
    json.dump(
        student,
        file,
        indent=4,
        ensure_ascii=False
    )

with path.open("r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded)
print(type(loaded))
print(loaded["marks"])

json_string = json.dumps(student)

print(json_string)

restored = json.loads(json_string)

print(restored == student)