'''
Example 04 — Accessing Values: Indexing vs get()
'''
student = {
    "name": "Amit",
    "age": 21,
    "marks": 85
}

print(student["name"])
print(student.get("marks"))

print(student.get("grade"))
print(student.get("grade", "Not Assigned"))

try:
    print(student["grade"])
except KeyError:
    print("Key does not exist")