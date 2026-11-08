'''
Example 11 — Argument Passing, Object Identity and Mutability
'''

def modify_integer(x):
    print("Before:", x, id(x))
    x += 10
    print("After:", x, id(x))


a = 100

modify_integer(a)

print("Outside:", a, id(a))


def modify_list(values):
    print("Before:", values, id(values))
    values.append(40)
    print("After:", values, id(values))


numbers = [10, 20, 30]

modify_list(numbers)

print("Outside:", numbers, id(numbers))