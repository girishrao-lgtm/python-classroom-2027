'''
Exercise 07 — Function-Based Calculator
'''
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None

    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

queries = [
    (10, 5, "+"),
    (10, 5, "-"),
    (10, 5, "*"),
    (10, 0, "/")
]

for a, b, operator in queries:
    result = operations[operator](a, b)
    print(a, operator, b, "=", result)
    