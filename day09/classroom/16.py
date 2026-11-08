'''
Example 16 — Closures and Function Factories
'''

def multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))


def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter1 = create_counter()
counter2 = create_counter()

print(counter1())
print(counter1())
print(counter2())
print(counter1())