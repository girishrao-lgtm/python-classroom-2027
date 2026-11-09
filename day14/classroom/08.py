'''
Example 08 — CSV Reading and Writing
'''
import csv

students = [
    ["Roll", "Name", "Marks"],
    [101, "Alice", 90],
    [102, "Bob", 85],
    [103, "Charlie", 95]
]

with open(
    "students.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:
    writer = csv.writer(file)
    writer.writerows(students)

with open(
    "students.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)