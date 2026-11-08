'''
Example 12 — Timing Decorator
'''
from functools import wraps
from time import perf_counter


def measure_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            end = perf_counter()
            print(f"Execution time: {end - start:.6f} seconds")

    return wrapper

@measure_time
def calculate():
    return sum(range(1_000_000))

print(calculate())
