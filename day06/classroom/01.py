'''
Classroom 01 — List Creation and Basic Operations
'''
numbers = [10, 20, 30, 40, 50]
mixed = [10, "Python", 3.14, True]
empty = []
nested = [[1, 2], [3, 4]]

print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Empty: {empty}")
print(f"Nested: {nested}")

print(f"Type: {type(numbers)}")
print(f"Length: {len(numbers)}")
print(f"Identity: {id(numbers)}")

print(f"First: {numbers[0]}")
print(f"Last: {numbers[-1]}")