'''
Example 17 — __slots__ and Attribute Storage
'''
class RegularStudent:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class SlottedStudent:

    __slots__ = ("marks", "name")

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = RegularStudent("Alice", 90)
student2 = SlottedStudent("Bob", 85)

print(student1.__dict__)

print(student2.name)
print(student2.marks)

student1.department = "CSE"

try:
    student2.department = "AI"
except AttributeError as error:
    print(error)