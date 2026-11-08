'''
Exercise 09 — Student Subject Performance
'''
students = {
    "Amit": {"Python": 85, "Java": 90, "SQL": 80},
    "Neha": {"Python": 95, "Java": 92, "SQL": 96},
    "Ravi": {"Python": 70, "Java": 75, "SQL": 78}
}

topper = None
best_average = -1

for name, subjects in students.items():
    average = sum(subjects.values()) / len(subjects)

    print(name, f"{average:.2f}")

    if average > best_average:
        best_average = average
        topper = name

print("Topper:", topper)