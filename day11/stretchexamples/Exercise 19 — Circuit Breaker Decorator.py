'''
Exercise 19 — Circuit Breaker Decorator
'''

from functools import wraps
from time import monotonic


def circuit_breaker(max_failures=3, reset_timeout=5):

    def decorator(func):

        failures = 0
        opened_at = None

        @wraps(func)
        def wrapper(*args, **kwargs):

            nonlocal failures, opened_at

            now = monotonic()

            if opened_at is not None:

                if now - opened_at < reset_timeout:
                    raise RuntimeError("Circuit is OPEN")

                opened_at = None
                failures = 0

            try:
                result = func(*args, **kwargs)

            except ConnectionError:

                failures += 1

                if failures >= max_failures:
                    opened_at = monotonic()

                raise

            failures = 0
            return result

        return wrapper

    return decorator

@circuit_breaker(max_failures=3)
def remote_service():
    raise ConnectionError("Service unavailable")

for _ in range(5):
    try:
        remote_service()
    except (ConnectionError, RuntimeError) as error:
        print(type(error).__name__, error)