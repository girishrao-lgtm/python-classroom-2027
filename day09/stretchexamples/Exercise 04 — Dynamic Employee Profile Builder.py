'''
Exercise 04 — Dynamic Employee Profile Builder
'''
def create_employee(emp_id, name, **details):
    employee = {
        "id": emp_id,
        "name": name
    }

    employee.update(details)

    return employee


e1 = create_employee(
    101,
    "Amit",
    department="AI",
    salary=80000,
    location="Bangalore"
)

e2 = create_employee(
    102,
    "Neha",
    department="CSE",
    experience=3
)

print(e1)
print(e2)