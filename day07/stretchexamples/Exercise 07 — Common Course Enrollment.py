'''
Exercise 07 — Common Course Enrollment
'''
python_students = {101, 102, 103, 104, 105}
java_students = {103, 104, 106, 107}

common = python_students & java_students

print("Both courses:", sorted(common))
print("Count:", len(common))