'''
Exercise 06 — Group Students by Department
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
    if department not in groups:
        groups[department] = []

    groups[department].append(name)

for department in sorted(groups):
    print(department, sorted(groups[department]))