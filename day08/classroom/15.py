'''
Example 15 — Nested Dictionaries
'''

students = {
    101: {
        "name": "Amit",
        "marks": {"Python": 85, "Java": 90}
    },
    102: {
        "name": "Neha",
        "marks": {"Python": 95, "Java": 92}
    }
}

for roll, details in students.items():
    print("Roll:", roll)
    print("Name:", details["name"])

    total = sum(details["marks"].values())
    average = total / len(details["marks"])

    print("Total:", total)
    print("Average:", average)

students[101]["marks"]["Python"] = 88

print(students)