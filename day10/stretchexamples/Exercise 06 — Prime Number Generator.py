'''
Exercise 06 — Prime Number Generator
'''

from itertools import islice


def prime_generator():
    primes = []
    number = 2

    while True:
        is_prime = True

        for prime in primes:
            if prime * prime > number:
                break

            if number % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(number)
            yield number

        number += 1


generator = prime_generator()

print(list(islice(generator, 15)))