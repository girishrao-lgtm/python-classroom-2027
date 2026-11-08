'''
Example 07 — Generator Functions and yield
'''

def generate_numbers():
    print("Generator started")

    yield 10

    print("After first yield")

    yield 20

    print("After second yield")

    yield 30

    print("Generator completed")


generator = generate_numbers()

print("Generator created")

print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print("Generator exhausted")

    