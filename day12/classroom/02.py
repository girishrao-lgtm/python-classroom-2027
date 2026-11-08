'''
Example 02 — Instance Attributes vs Class Attributes
'''
class Student:
    college = "ABC Engineering College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Alice", 90)
student2 = Student("Bob", 85)

print(student1.college)
print(student2.college)

Student.college = "XYZ University"

print(student1.college)
print(student2.college)

student1.college = "Private College"

print(student1.college)
print(student2.college)

print(student1.__dict__)
print(Student.__dict__["college"])