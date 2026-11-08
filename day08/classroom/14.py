'''
Example 14 — Grouping Elements Using Dictionaries
'''

students = [
    ("Amit", "CSE"),
    ("Neha", "AI"),
    ("Ravi", "CSE"),
    ("Priya", "AI"),
    ("Karan", "ECE")
]

groups = {}

for name, department in students:
    groups.setdefault(department, []).append(name)

for department, names in groups.items():
    print(department, names)