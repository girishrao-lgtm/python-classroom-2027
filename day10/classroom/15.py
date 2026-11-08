'''
Example 15 — itertools.count(), cycle() and repeat()
'''

from itertools import count, cycle, islice, repeat

numbers = count(start=10, step=5)

print(list(islice(numbers, 5)))

colors = cycle(["RED", "GREEN", "BLUE"])

print(list(islice(colors, 8)))

values = repeat("PYTHON", 4)

print(list(values))