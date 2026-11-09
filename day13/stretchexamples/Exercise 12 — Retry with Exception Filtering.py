'''
Exercise 12 — Retry with Exception Filtering
'''
from functools import wraps
from time import sleep


def retry(
    attempts=3,
    delay=0.1,
    exceptions=(ConnectionError,)
):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)

                except exceptions:
                    if attempt == attempts:
                        raise

                    sleep(delay * attempt)

        return wrapper

    return decorator


counter = 0


@retry(attempts=4)
def fetch_data():
    global counter
    counter += 1

    if counter < 3:
        raise ConnectionError("Temporary failure")

    return {"status": "success"}


print(fetch_data())