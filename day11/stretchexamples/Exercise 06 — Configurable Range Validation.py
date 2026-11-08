'''
Exercise 06 — Configurable Range Validation
'''

from functools import wraps


def validate_range(minimum, maximum):

    def decorator(func):

        @wraps(func)
        def wrapper(value):

            if not minimum <= value <= maximum:
                raise ValueError("Value outside allowed range")

            return func(value)

        return wrapper

    return decorator

@validate_range(0, 100)
def assign_grade(mark):

    if mark >= 90:
        return "A"

    if mark >= 75:
        return "B"

    if mark >= 60:
        return "C"

    return "D"

print(assign_grade(95))
print(assign_grade(72))