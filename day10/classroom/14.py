'''
Example 14 — Infinite Generators and Controlled Consumption
'''

from itertools import islice


def natural_numbers():
    number = 1

    while True:
        yield number
        number += 1


generator = natural_numbers()

first_ten = list(islice(generator, 10))

print(first_ten)

next_five = list(islice(generator, 5))

print(next_five)