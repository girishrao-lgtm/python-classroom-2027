'''
Example 03 — How a for Loop Works Internally
'''
numbers = [10, 20, 30]

print("Using for loop")

for number in numbers:
    print(number)

print("Manual implementation")

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
    except StopIteration:
        break

    print(number)