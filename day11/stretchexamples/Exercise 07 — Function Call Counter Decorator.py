'''
Exercise 07 — Function Call Counter Decorator
'''

from functools import wraps


def count_calls(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0

    return wrapper

@count_calls
def square(number):
    return number * number

print(square(5))
print(square(6))
print(square(7))

print("Total calls:", square.calls)