'''
Example 20 — Function-Based Student Assessment System
'''

def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def determine_grade(average):
    if average >= 90:
        return "A"

    if average >= 75:
        return "B"

    if average >= 60:
        return "C"

    if average >= 40:
        return "D"

    return "F"


def generate_report(name, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = determine_grade(average)

    return {
        "name": name,
        "total": total,
        "average": average,
        "grade": grade
    }


students = {
    "Amit": [80, 90, 85],
    "Neha": [95, 92, 96],
    "Ravi": [45, 55, 60]
}

for name, marks in students.items():
    report = generate_report(name, marks)
    print(report)