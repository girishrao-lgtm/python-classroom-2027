'''
Exercise 14 — Callable Objects Using __call__
'''
class Multiplier:

    def __init__(self, factor):
        self.factor = factor
        self.calls = 0

    def __call__(self, number):
        self.calls += 1
        return number * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(10))
print(double(20))
print(triple(10))

print("Double calls:", double.calls)
print("Triple calls:", triple.calls)

