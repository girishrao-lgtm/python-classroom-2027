'''
Example 18 — Recursive Fibonacci and Memoization
'''

from functools import lru_cache, cache


def fibonacci_recursive(n):
    if n <= 1:
        return n

    return (
        fibonacci_recursive(n - 1)
        + fibonacci_recursive(n - 2)
    )


@cache
def fibonacci_memo(n):
    if n <= 1:
        return n

    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


print(fibonacci_recursive(10))
print(fibonacci_memo(40))

print(fibonacci_memo.cache_info())