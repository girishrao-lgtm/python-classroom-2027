'''
Exercise 01 — Dynamic Calculator Using Function Registry
'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

requests = [
    ("add", 10, 20),
    ("multiply", 5, 6),
    ("divide", 20, 4)
]

for operation, a, b in requests:
    result = operations[operation](a, b)
    print(operation, result)