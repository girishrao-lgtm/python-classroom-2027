'''
Classroom 11 — List Comprehensions
'''
numbers = list(range(1, 11))

squares = [x * x for x in numbers]

evens = [x for x in numbers if x % 2 == 0]

odd_squares = [x * x for x in numbers if x % 2 != 0]

labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(squares)
print(evens)
print(odd_squares)
print(labels)
