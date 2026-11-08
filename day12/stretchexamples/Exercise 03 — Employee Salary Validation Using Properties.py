'''
Exercise 03 — Employee Salary Validation Using Properties
'''

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Invalid salary")

        self._salary = value

    def increment(self, percentage):
        if percentage < 0:
            raise ValueError("Invalid percentage")

        self.salary *= 1 + percentage / 100


employee = Employee("Alice", 50000)

employee.increment(10)

print(employee.salary)

try:
    employee.salary = -100
except ValueError as error:
    print(error)