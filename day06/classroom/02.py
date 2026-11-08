'''
Classroom 02 — Positive and Negative Indexing
'''
numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

print("Negative indexing:")

for i in range(-len(numbers), 0):
    print(f"Index {i}: {numbers[i]}")

try:
    print(numbers[10])
except IndexError as error:
    print(f"Error: {error}")