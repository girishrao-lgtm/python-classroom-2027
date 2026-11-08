'''
Exercise 20 — Modular Student Assessment Engine
'''

def validate_marks(marks):
    return bool(marks) and all(0 <= mark <= 100 for mark in marks)


def calculate_statistics(marks):
    total = sum(marks)
    average = total / len(marks)

    return total, average


def assign_grade(average):
    if average >= 90:
        return "A"

    if average >= 75:
        return "B"

    if average >= 60:
        return "C"

    if average >= 40:
        return "D"

    return "F"


def generate_report(name, *marks, passing_marks=40, **details):
    if not validate_marks(marks):
        return {"name": name, "error": "Invalid marks"}

    total, average = calculate_statistics(marks)

    status = (
        "PASS"
        if all(mark >= passing_marks for mark in marks)
        else "FAIL"
    )

    return {
        "name": name,
        "total": total,
        "average": round(average, 2),
        "grade": assign_grade(average) if status == "PASS" else "F",
        "status": status,
        **details
    }


students = [
    ("Amit", [85, 90, 88]),
    ("Neha", [95, 96, 92]),
    ("Ravi", [45, 35, 70])
]

for name, marks in students:
    report = generate_report(
        name,
        *marks,
        passing_marks=40,
        batch="2027",
        department="CSE"
    )

    print(report)