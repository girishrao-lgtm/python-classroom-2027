'''
Example 16 — Memoization Using lru_cache
'''
from functools import cache


@cache
def fibonacci(n):

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(35))
print(fibonacci.cache_info())

print(fibonacci(35))
print(fibonacci.cache_info())