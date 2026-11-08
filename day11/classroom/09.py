'''
Example 09 — Preserving Metadata Using functools.wraps
'''
from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)
        return func(*args, **kwargs)

    return wrapper

@decorator
def calculate_area(length, breadth):
    """Calculate rectangle area."""
    return length * breadth

print(calculate_area(5, 10))

print(calculate_area.__name__)
print(calculate_area.__doc__)
print(calculate_area.__wrapped__)