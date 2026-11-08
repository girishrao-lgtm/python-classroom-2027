'''
Example 04 — Instance, Class and Static Methods
'''

class Employee:

    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display(self):
        print(self.name, self.salary)

    @classmethod
    def total_employees(cls):
        return cls.employee_count

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

employee1.display()
employee2.display()

print(Employee.total_employees())
print(Employee.is_valid_salary(45000))
print(Employee.is_valid_salary(-100))