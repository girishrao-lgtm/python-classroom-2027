'''
Example 02 — Positional and Keyword Arguments
'''
def student_details(name, age, marks):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Marks: {marks}")


student_details("Amit", 21, 85)

student_details(
    marks=95,
    name="Neha",
    age=22
)

student_details("Ravi", marks=78, age=20)