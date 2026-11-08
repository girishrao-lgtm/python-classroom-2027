'''
Example 04 — Positional-Only and Keyword-Only Parameters
'''
def calculate(a, b, /, *, operation="add"):
    if operation == "add":
        return a + b

    if operation == "multiply":
        return a * b

    return None


print(calculate(10, 20))
print(calculate(10, 20, operation="multiply"))

try:
    print(calculate(a=10, b=20))
except TypeError as e:
    print(type(e).__name__, e)


def register(name, *, department, year):
    print(name, department, year)


register("Amit", department="CSE", year=2027)