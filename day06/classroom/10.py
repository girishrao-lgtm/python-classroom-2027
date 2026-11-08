'''
Classroom 10 — Traversal Techniques
'''
numbers = [10, 20, 30, 40, 50]

print("Direct traversal:")

for number in numbers:
    print(number)

print("Index traversal:")

for i in range(len(numbers)):
    print(i, numbers[i])

print("Enumerate:")

for index, value in enumerate(numbers):
    print(index, value)

print("While traversal:")

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1