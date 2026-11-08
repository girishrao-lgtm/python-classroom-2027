'''
Example 09 — Tuple Sorting and Multiple Sort Keys
'''
students = [
    ("Amit", 85),
    ("Ravi", 92),
    ("Neha", 85),
    ("Priya", 95),
    ("Arun", 85)
]

print(sorted(students))

by_marks = sorted(students, key=lambda x: x[1])
print(by_marks)

descending = sorted(students, key=lambda x: -x[1])
print(descending)

ranked = sorted(students, key=lambda x: (-x[1], x[0]))
print(ranked)