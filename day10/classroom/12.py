'''
Example 12 — Generator send() and Two-Way Communication
'''

def accumulator():
    total = 0

    while True:
        value = yield total

        if value is not None:
            total += value


generator = accumulator()

print(next(generator))

print(generator.send(10))
print(generator.send(20))
print(generator.send(30))
print(generator.send(-5))

generator.close()
