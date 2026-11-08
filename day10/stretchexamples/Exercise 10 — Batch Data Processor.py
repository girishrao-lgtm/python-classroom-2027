'''
Exercise 10 — Batch Data Processor
'''

from itertools import islice


def batch_generator(iterable, batch_size):
    if batch_size <= 0:
        raise ValueError("Batch size must be positive")

    iterator = iter(iterable)

    while True:
        batch = list(islice(iterator, batch_size))

        if not batch:
            break

        yield batch


numbers = range(1, 21)

for batch in batch_generator(numbers, 6):
    print(batch)