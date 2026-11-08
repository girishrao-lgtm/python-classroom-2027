'''
Example 01 — Iterable vs Iterator
'''
numbers = [10, 20, 30, 40]

print("List:", numbers)
print("Iterable:", hasattr(numbers, "__iter__"))
print("Iterator:", hasattr(numbers, "__next__"))

iterator = iter(numbers)

print("Iterator object:", iterator)
print("Iterable:", hasattr(iterator, "__iter__"))
print("Iterator:", hasattr(iterator, "__next__"))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
