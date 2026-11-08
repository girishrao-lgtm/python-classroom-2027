'''
Exercise 03 — Reusable Range Iterable
'''
class CustomRange:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise ValueError("Step cannot be zero")

        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        current = self.start

        if self.step > 0:
            while current < self.stop:
                yield current
                current += self.step
        else:
            while current > self.stop:
                yield current
                current += self.step


numbers = CustomRange(2, 12, 2)

print(list(numbers))
print(list(numbers))

print(list(CustomRange(10, 0, -2)))