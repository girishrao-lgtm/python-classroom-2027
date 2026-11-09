'''
Exercise 02 — Robust Calculator with Custom Exceptions
'''
class CalculatorError(Exception):
    pass


class InvalidOperationError(CalculatorError):
    pass


class DivisionByZeroError(CalculatorError):
    pass


def calculate(a, b, operation):
    operations = {
        "+": lambda: a + b,
        "-": lambda: a - b,
        "*": lambda: a * b,
        "/": lambda: a / b
    }

    if operation not in operations:
        raise InvalidOperationError("Unsupported operation")

    if operation == "/" and b == 0:
        raise DivisionByZeroError("Cannot divide by zero")

    return operations[operation]()


requests = [
    (10, 5, "+"),
    (20, 0, "/"),
    (10, 3, "%"),
    (8, 2, "*")
]

for request in requests:
    try:
        print(calculate(*request))

    except CalculatorError as error:
        print(type(error).__name__, error)