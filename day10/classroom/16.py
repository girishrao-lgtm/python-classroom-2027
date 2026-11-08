'''
Example 16 — itertools.chain(), islice() and accumulate()
'''
from itertools import chain, islice, accumulate

a = [1, 2, 3]
b = [4, 5]
c = [6, 7]

combined = chain(a, b, c)

print(list(combined))

numbers = range(100)

print(list(islice(numbers, 10, 20, 2)))

values = [10, 20, 30, 40]

print(list(accumulate(values)))
print(list(accumulate(values, max)))