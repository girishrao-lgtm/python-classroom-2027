'''
Example 05 — Custom Iterator Using __iter__() and __next__()
'''

class NumberIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


numbers = NumberIterator(1, 5)

for number in numbers:
    print(number)

print("Second traversal:", list(numbers))
