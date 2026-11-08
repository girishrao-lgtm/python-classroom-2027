'''
Example 02 — Understanding iter(), next() and StopIteration
'''
numbers = [5, 10, 15]

iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        print("Iteration completed")
        break

iterator = iter(numbers)

print(next(iterator, "END"))
print(next(iterator, "END"))
print(next(iterator, "END"))
print(next(iterator, "END"))
