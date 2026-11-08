'''
Exercise 02 — Employee Record Unpacking
'''
employees = [
    ("E101", "Amit", "Development", "Testing"),
    ("E102", "Neha", "AI"),
    ("E103", "Ravi", "Backend", "Cloud", "DevOps")
]

for emp_id, name, *projects in employees:
    print("ID:", emp_id)
    print("Name:", name)
    print("Projects:", projects)
    print("Project Count:", len(projects))