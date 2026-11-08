'''
Example 07 — Nested Tuples and Traversal
'''
students = (
    ("Amit", (80, 85, 90)),
    ("Ravi", (70, 75, 80)),
    ("Neha", (95, 92, 96))
)

for name, marks in students:
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    print(f"{name}: Total={total}, Average={average:.2f}")
    