'''
Example 13 — Abstract Base Classes
'''

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


shapes = [
    Rectangle(10, 5),
    Circle(7)
]

for shape in shapes:
    print(shape.area())

try:
    shape = Shape()
except TypeError as error:
    print(error)