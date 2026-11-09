'''
Example 18 — Timing Context Manager
'''

from contextlib import contextmanager
from time import perf_counter


@contextmanager
def timer(label):
    start = perf_counter()

    try:
        yield

    finally:
        elapsed = perf_counter() - start
        print(f"{label}: {elapsed:.6f} seconds")


with timer("Sum calculation"):
    result = sum(range(1_000_000))

print(result)