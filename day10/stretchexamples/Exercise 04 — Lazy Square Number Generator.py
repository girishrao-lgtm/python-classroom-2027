'''
Exercise 04 — Lazy Square Number Generator
'''
def square_generator(numbers):
    for number in numbers:
        print("Processing:", number)
        yield number * number


numbers = [1, 2, 3, 4, 5]

generator = square_generator(numbers)

print(next(generator))
print(next(generator))

print(list(generator))