'''
Exercise 04 — CSV Student Result Analyzer
'''
import csv
from collections import defaultdict

records = [
    {"name": "Alice", "department": "AI", "marks": 90},
    {"name": "Bob", "department": "CSE", "marks": 85},
    {"name": "Charlie", "department": "AI", "marks": 95},
    {"name": "David", "department": "CSE", "marks": 70}
]

with open("results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "department", "marks"]
    )
    writer.writeheader()
    writer.writerows(records)

departments = defaultdict(list)

with open("results.csv", "r", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        departments[row["department"]].append(
            int(row["marks"])
        )

for department, marks in departments.items():
    print(
        department,
        "Average:", sum(marks) / len(marks),
        "Highest:", max(marks)
    )