'''
Example 15 — Higher-Order Functions: map(), filter(), reduce()
'''

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squares = [x * x for x in numbers]

print("Squares:", squares)

evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Evens:", evens)

total = reduce(lambda a, b: a + b, numbers)

print("Total:", total)

product = reduce(lambda a, b: a * b, numbers, 1)

print("Product:", product)