'''
Example 01 — Creating Classes and Objects
'''

class Student:
    pass


student1 = Student()
student2 = Student()

student1.name = "Alice"
student1.marks = 90

student2.name = "Bob"
student2.marks = 85

print(student1.name, student1.marks)
print(student2.name, student2.marks)

print(type(student1))
print(student1 is student2)
print(student1.__dict__)