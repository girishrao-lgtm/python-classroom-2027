'''
Example 04 — Iterator Exhaustion and Independent Iterators
'''

numbers = [10, 20, 30]

iterator1 = iter(numbers)
iterator2 = iter(numbers)

print(next(iterator1))
print(next(iterator1))

print(next(iterator2))

print(list(iterator1))
print(list(iterator2))

print("Exhausted:", list(iterator1))

fresh_iterator = iter(numbers)
print("Fresh:", list(fresh_iterator))