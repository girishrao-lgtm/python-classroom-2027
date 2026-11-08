'''
Classroom 04 — List Mutability
'''
numbers = [10, 20, 30, 40]

print(f"Before: {numbers}")
print(f"Identity before: {id(numbers)}")

numbers[1] = 200
numbers[-1] = 400

print(f"After: {numbers}")
print(f"Identity after: {id(numbers)}")

numbers[1:3] = [7, 8, 9]

print(f"After slice assignment: {numbers}")