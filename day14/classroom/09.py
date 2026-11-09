'''
Example 09 — CSV Dictionary Processing
'''
import csv

employees = [
    {"id": 101, "name": "Alice", "salary": 50000},
    {"id": 102, "name": "Bob", "salary": 60000},
    {"id": 103, "name": "Charlie", "salary": 55000}
]

fields = ["id", "name", "salary"]

with open(
    "employees.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()
    writer.writerows(employees)

with open(
    "employees.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:
    reader = csv.DictReader(file)

    total = 0

    for employee in reader:
        salary = int(employee["salary"])
        total += salary

        print(employee["name"], salary)

print("Total salary:", total)