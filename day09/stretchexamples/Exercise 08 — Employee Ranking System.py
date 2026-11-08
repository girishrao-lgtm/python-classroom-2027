'''
Exercise 08 — Employee Ranking System
'''
employees = [
    ("Amit", 85000, 4),
    ("Neha", 95000, 3),
    ("Ravi", 85000, 6),
    ("Priya", 95000, 5)
]

ranked = sorted(
    employees,
    key=lambda e: (-e[1], -e[2], e[0])
)

for rank, employee in enumerate(ranked, 1):
    print(rank, employee)