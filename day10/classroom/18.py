'''
Example 18 — itertools.product(), permutations() and combinations()
'''
from itertools import combinations, permutations, product

a = [1, 2]
b = ["A", "B"]

print("Cartesian product")
print(list(product(a, b)))

numbers = [1, 2, 3]

print("Permutations")
print(list(permutations(numbers, 2)))

print("Combinations")
print(list(combinations(numbers, 2)))
