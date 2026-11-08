'''
Example 06 — Reusable Iterable with Independent Iterators
'''
class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start

        while current <= self.end:
            yield current
            current += 1


numbers = NumberRange(1, 5)

print(list(numbers))
print(list(numbers))

iterator1 = iter(numbers)
iterator2 = iter(numbers)

print(next(iterator1))
print(next(iterator1))
print(next(iterator2))
