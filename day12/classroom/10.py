'''
Example 10 — Single and Multilevel Inheritance
'''
class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Employee(Person):

    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print("Employee ID:", self.employee_id)


class Manager(Employee):

    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


manager = Manager("Alice", 101, "Engineering")

manager.display()

print(isinstance(manager, Person))
print(isinstance(manager, Employee))
print(isinstance(manager, Manager))