'''
Example 15 — Retry Decorator with Configurable Attempts
'''

from functools import wraps


def retry(attempts):

    if attempts < 1:
        raise ValueError("Attempts must be positive")

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)

                except ConnectionError:
                    print(f"Attempt {attempt} failed")

                    if attempt == attempts:
                        raise

        return wrapper

    return decorator

counter = 0

@retry(3)
def connect():
    global counter
    counter += 1

    if counter < 3:
        raise ConnectionError("Connection failed")

    return "Connected"

print(connect())