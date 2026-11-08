'''
Example 08 — Decorators with Arguments and Return Values
'''
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

        result = func(*args, **kwargs)

        print("Result:", result)

        return result

    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(10, 20))
print(add(a=30, b=40))
