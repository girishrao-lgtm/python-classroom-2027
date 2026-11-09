'''
Example 03 — Handling Multiple Exception Types
'''
requests = [
    (10, 2),
    (20, 0),
    ("abc", 5),
    (30, 3)
]

for a, b in requests:
    try:
        result = a / b

    except ZeroDivisionError:
        print("Cannot divide by zero")

    except TypeError:
        print("Invalid operand type")

    else:
        print("Result:", result)