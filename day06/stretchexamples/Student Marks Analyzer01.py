'''
Stretch 01 — Student Marks Analyzer
'''
n = int(input("Number of students: "))

marks = []

for i in range(n):
    mark = int(input(f"Student {i + 1} marks: "))
    marks.append(mark)

if not marks:
    print("No student records")
else:
    print(f"Highest: {max(marks)}")
    print(f"Lowest: {min(marks)}")
    print(f"Average: {sum(marks) / n:.2f}")

    passed = 0

    for mark in marks:
        if mark >= 40:
            passed += 1

    print(f"Passed: {passed}")
    print(f"Failed: {n - passed}")