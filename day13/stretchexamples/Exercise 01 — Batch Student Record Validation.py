'''
Exercise 01 — Batch Student Record Validation
'''
class StudentValidationError(Exception):
    pass


def validate_student(student):
    if "name" not in student:
        raise StudentValidationError("Name missing")

    if "marks" not in student:
        raise StudentValidationError("Marks missing")

    marks = student["marks"]

    if not isinstance(marks, (int, float)):
        raise StudentValidationError("Marks must be numeric")

    if not 0 <= marks <= 100:
        raise StudentValidationError("Marks outside range")

    return True


students = [
    {"name": "Alice", "marks": 90},
    {"name": "Bob", "marks": 120},
    {"name": "Charlie"},
    {"name": "David", "marks": 75}
]

valid_students = []
invalid_students = []

for student in students:
    try:
        validate_student(student)
        valid_students.append(student)

    except StudentValidationError as error:
        invalid_students.append((student, str(error)))


print("Valid:", valid_students)
print("Invalid:", invalid_students)