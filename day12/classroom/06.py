'''
Example 06 — Public, Protected Convention and Name Mangling
'''

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._department = "Engineering"
        self.__salary = salary

    def display(self):
        print(self.name)
        print(self._department)
        print(self.__salary)

    def get_salary(self):
        return self.__salary


employee = Employee("Alice", 50000)

employee.display()

print(employee.name)
print(employee._department)
print(employee.get_salary())

print(employee.__dict__)
print(employee._Employee__salary)
