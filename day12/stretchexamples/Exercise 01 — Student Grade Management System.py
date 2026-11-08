'''
Exercise 01 — Student Grade Management System
'''
class Student:

    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        if self.marks >= 75:
            return "B"
        if self.marks >= 60:
            return "C"
        return "D"

    def __repr__(self):
        return (
            f"Student({self.roll_number}, "
            f"{self.name!r}, {self.marks})"
        )


students = [
    Student(101, "Alice", 88),
    Student(102, "Bob", 95),
    Student(103, "Charlie", 76)
]

for student in students:
    print(student.name, student.grade())

topper = max(students, key=lambda student: student.marks)

print("Topper:", topper)