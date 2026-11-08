'''
Exercise 05 — Input Validation Decorator
'''

from functools import wraps


def validate_positive(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        values = list(args) + list(kwargs.values())

        for value in values:
            if type(value) not in (int, float) or value <= 0:
                raise ValueError("All inputs must be positive numbers")

        return func(*args, **kwargs)

    return wrapper

@validate_positive
def calculate_area(length, breadth):
    return length * breadth

print(calculate_area(10, 20))

try:
    print(calculate_area(-5, 10))
except ValueError as error:
    print(error)