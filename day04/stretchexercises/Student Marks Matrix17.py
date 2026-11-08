'''
Stretch 17 — Student Marks Matrix
Read marks for N students across M subjects. Calculate each student's total and average.

'''
students = int(input("Number of students: "))
subjects = int(input("Number of subjects: "))

for student in range(1, students + 1):

    total = 0

    for subject in range(1, subjects + 1):

        marks = float(
            input(f"Student {student}, Subject {subject}: ")
        )

        total += marks

    if subjects > 0:
        average = total / subjects
    else:
        average = 0

    print(f"Student {student} total = {total}")
    print(f"Student {student} average = {average:.2f}")