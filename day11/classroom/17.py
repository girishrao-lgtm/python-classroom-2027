'''
Example 17 — Pure Functions and Immutability
'''
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Employee:
    name: str
    salary: int

def increase_salary(employee, percentage):
    new_salary = employee.salary * (1 + percentage / 100)

    return replace(
        employee,
        salary=round(new_salary)
    )

original = Employee("Alice", 50000)

updated = increase_salary(original, 10)

print(original)
print(updated)