'''
Example 16 — Dataclasses and Immutable Objects
'''
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Student:
    roll_number: int
    name: str
    marks: int


student1 = Student(101, "Alice", 90)

student2 = replace(student1, marks=95)

print(student1)
print(student2)

print(student1 == student2)

try:
    student1.marks = 100
except AttributeError as error:
    print(type(error).__name__)