'''
Find Common Registered Students
'''
course_a = [101, 102, 103, 104, 105]
course_b = [103, 104, 106, 107]

registered_b = set(course_b)

common = []
seen = set()

for student in course_a:

    if student in registered_b and student not in seen:
        common.append(student)
        seen.add(student)

print(f"Common students: {common}")