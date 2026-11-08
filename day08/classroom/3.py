'''
Example 03 — Duplicate Keys and Key Equality
'''

data = {
    "A": 10,
    "B": 20,
    "A": 30  # noqa: F601
}

print(data)

numbers = {
    1: "Integer",
    1.0: "Float"  # noqa: F601
}

print(numbers)
print(len(numbers))

print(1 == True)
print(1 == 1.0)

print(hash(1))
print(hash(True))
print(hash(1.0))