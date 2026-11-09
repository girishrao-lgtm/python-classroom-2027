'''
Example 07 — Re-Raising Exceptions
'''
def calculate(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Error recorded inside calculate")
        raise


try:
    calculate(10, 0)

except ZeroDivisionError:
    print("Caller handled the exception")