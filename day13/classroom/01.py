'''
Example 01 — Exception Hierarchy and Built-in Exceptions
'''

exceptions = [
    ValueError("Invalid value"),
    TypeError("Invalid type"),
    ZeroDivisionError("Division by zero"),
    KeyError("Missing key"),
    IndexError("Invalid index"),
    FileNotFoundError("File missing")
]

for error in exceptions:
    print(type(error).__name__)
    print(isinstance(error, Exception))
    print(isinstance(error, BaseException))
    print(type(error).__mro__)
    print("-" * 40)