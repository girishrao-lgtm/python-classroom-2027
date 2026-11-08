'''
Example 19 — Memory Efficiency of Generators
'''
import sys

n = 1_000_000

numbers_list = [x * x for x in range(n)]
numbers_generator = (x * x for x in range(n))

print("List object bytes:", sys.getsizeof(numbers_list))
print("Generator object bytes:", sys.getsizeof(numbers_generator))

print("First generator value:", next(numbers_generator))
print("Second generator value:", next(numbers_generator))

print("List length:", len(numbers_list))