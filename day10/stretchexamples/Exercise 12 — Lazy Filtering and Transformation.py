'''
Exercise 12 — Lazy Filtering and Transformation
'''

def source():
    for number in range(1, 21):
        yield number


def filter_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def square_numbers(numbers):
    for number in numbers:
        yield number * number


pipeline = square_numbers(filter_even(source()))

print(list(pipeline))
