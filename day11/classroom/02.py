'''
Example 02 — Functions as Arguments and Return Values
'''
def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_operation(operation, value):
    return operation(value)

def choose_operation(name):
    if name == "square":
        return square
    return cube

print(apply_operation(square, 5))
print(apply_operation(cube, 3))

operation = choose_operation("square")
print(operation(6))
