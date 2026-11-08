'''
Exercise 01 — Student Result Processing
'''

def process_result(name, marks):
    total = sum(marks)
    average = total / len(marks)

    status = "PASS" if all(mark >= 40 for mark in marks) else "FAIL"

    return name, total, average, status


students = [
    ("Amit", [80, 85, 90]),
    ("Neha", [95, 92, 96]),
    ("Ravi", [50, 35, 70])
]

for name, marks in students:
    result = process_result(name, marks)
    print(result)