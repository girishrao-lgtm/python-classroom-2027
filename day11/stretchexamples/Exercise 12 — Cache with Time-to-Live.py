'''
Exercise 12 — Cache with Time-to-Live
'''

from functools import wraps
from time import monotonic, sleep


def ttl_cache(seconds):

    def decorator(func):

        cache = {}

        @wraps(func)
        def wrapper(*args):

            now = monotonic()

            if args in cache:
                value, expiry = cache[args]

                if now < expiry:
                    print("Cache hit")
                    return value

            print("Cache miss")

            result = func(*args)

            cache[args] = (result, monotonic() + seconds)

            return result

        return wrapper

    return decorator

@ttl_cache(seconds=2)
def calculate_square(number):
    return number * number

print(calculate_square(10))
print(calculate_square(10))

sleep(2.1)

print(calculate_square(10))