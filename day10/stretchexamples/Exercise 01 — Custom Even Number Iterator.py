'''
Exercise 01 — Custom Even Number Iterator
'''

class EvenIterator:
    def __init__(self, start, end):
        self.current = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 2

        return value


iterator = EvenIterator(3, 15)

for number in iterator:
    print(number)
    