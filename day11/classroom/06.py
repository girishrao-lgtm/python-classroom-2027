'''
Example 06 — Building a Decorator Manually
'''
def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

def greet():
    print("Hello Python")

greet = decorator(greet)

greet()