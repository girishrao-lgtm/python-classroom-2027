'''
Exercise 01 — Student Grade Management
'''
students = {
    101: 85,
    102: 90,
    103: 72
}

students[104] = 88
students[102] = 95

roll = 103

students.pop(roll, None)

for roll, marks in students.items():
    grade = "A" if marks >= 90 else "B" if marks >= 75 else "C"
    print(roll, marks, grade)