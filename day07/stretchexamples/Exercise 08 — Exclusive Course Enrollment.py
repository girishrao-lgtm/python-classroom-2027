'''
Exercise 08 — Exclusive Course Enrollment
'''
python_students = {101, 102, 103, 104}
java_students = {103, 104, 105, 106}

exclusive = python_students ^ java_students

print("Exactly one course:", sorted(exclusive))
print("Count:", len(exclusive))