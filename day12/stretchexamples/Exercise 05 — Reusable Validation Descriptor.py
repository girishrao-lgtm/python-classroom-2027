'''
Exercise 05 — Reusable Validation Descriptor
'''
class RangeValidator:

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

    def __set_name__(self, owner, name):
        self.storage_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Numeric value required")

        if not self.minimum <= value <= self.maximum:
            raise ValueError("Value outside range")

        setattr(instance, self.storage_name, value)


class Student:

    marks = RangeValidator(0, 100)
    attendance = RangeValidator(0, 100)

    def __init__(self, marks, attendance):
        self.marks = marks
        self.attendance = attendance


student = Student(90, 85)

print(student.marks)
print(student.attendance)

try:
    student.marks = 120
except ValueError as error:
    print(error)
    
