'''
Example 08 — Read-Only Computed Properties
'''

class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    @property
    def area(self):
        return self.length * self.breadth

    @property
    def perimeter(self):
        return 2 * (self.length + self.breadth)


rectangle = Rectangle(10, 5)

print(rectangle.area)
print(rectangle.perimeter)

rectangle.length = 20

print(rectangle.area)

try:
    rectangle.area = 500
except AttributeError as error:
    print(error)
    