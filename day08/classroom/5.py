'''
Example 05 — Insertion, Updating and Deletion
'''
student = {"name": "Amit", "marks": 80}

student["age"] = 21
student["marks"] = 90

print(student)

student.update({"city": "Bangalore", "grade": "A"})
print(student)

removed = student.pop("city")
print("Removed:", removed)

last = student.popitem()
print("Last inserted pair:", last)

del student["age"]

print(student)

student.clear()
print(student)