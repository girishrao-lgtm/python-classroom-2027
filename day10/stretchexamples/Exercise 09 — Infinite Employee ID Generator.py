'''
Exercise 09 — Infinite Employee ID Generator
'''
from itertools import islice


def employee_ids(prefix="EMP", start=1):
    number = start

    while True:
        yield f"{prefix}{number:04d}"
        number += 1


generator = employee_ids()

print(list(islice(generator, 10)))