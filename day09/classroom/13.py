'''
Example 13 — First-Class Functions and Function References
'''

def square(x):
    return x * x


def cube(x):
    return x * x * x


operation = square

print(operation(5))

operation = cube

print(operation(5))

operations = {
    "square": square,
    "cube": cube
}

for name, function in operations.items():
    print(name, function(4))


def execute(function, value):
    return function(value)


print(execute(square, 6))
print(execute(cube, 3))
