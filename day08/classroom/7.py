'''
Example 07 — Dictionary Views: keys(), values(), items()
'''
student = {
    "name": "Neha",
    "age": 22,
    "marks": 95
}

keys = student.keys()
values = student.values()
items = student.items()

print(keys)
print(values)
print(items)

student["grade"] = "A"

print(keys)
print(values)
print(items)

print("name" in keys)
print(("marks", 95) in items)