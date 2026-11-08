'''
Exercise 09 — Retry with Exponential Backoff
'''

from functools import wraps
from time import sleep


def retry(attempts=3, delay=0.1):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(attempts):

                try:
                    return func(*args, **kwargs)

                except ConnectionError:

                    if attempt == attempts - 1:
                        raise

                    wait = delay * (2 ** attempt)

                    print(f"Retrying after {wait:.2f}s")
                    sleep(wait)

        return wrapper

    return decorator

counter = 0

@retry(attempts=4, delay=0.1)
def fetch_data():
    global counter
    counter += 1

    if counter < 3:
        raise ConnectionError("Temporary failure")

    return {"status": "success"}

print(fetch_data())