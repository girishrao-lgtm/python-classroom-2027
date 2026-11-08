'''
Example 10 — Stacked Decorators and Execution Order
'''

from functools import wraps


def first(func):

    @wraps(func)
    def wrapper():
        print("First decorator before")
        result = func()
        print("First decorator after")
        return result

    return wrapper

def second(func):

    @wraps(func)
    def wrapper():
        print("Second decorator before")
        result = func()
        print("Second decorator after")
        return result

    return wrapper

@first
@second
def display():
    print("Original function")

display()