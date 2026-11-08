'''
Exercise 08 — Exception Handling with Default Return Value
'''

from functools import wraps


def safe_execute(default=None):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            try:
                return func(*args, **kwargs)

            except (ValueError, ZeroDivisionError) as error:
                print("Error:", error)
                return default

        return wrapper

    return decorator

@safe_execute(default=0)
def divide(a, b):
    return a / b

print(divide(20, 5))
print(divide(20, 0))