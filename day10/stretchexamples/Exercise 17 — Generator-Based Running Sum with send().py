'''
Exercise 17 — Generator-Based Running Sum with send()
'''
def running_sum():
    total = 0

    while True:
        value = yield total

        if value == "RESET":
            total = 0
        elif value is not None:
            total += value


generator = running_sum()

print(next(generator))
print(generator.send(10))
print(generator.send(20))
print(generator.send("RESET"))
print(generator.send(50))

generator.close()