'''
Exercise 10 — Rate Limiter Using a Decorator
'''

from collections import deque
from functools import wraps
from time import monotonic


def rate_limit(max_calls, period):

    def decorator(func):

        timestamps = deque()

        @wraps(func)
        def wrapper(*args, **kwargs):

            now = monotonic()

            while timestamps and now - timestamps[0] >= period:
                timestamps.popleft()

            if len(timestamps) >= max_calls:
                raise RuntimeError("Rate limit exceeded")

            timestamps.append(now)

            return func(*args, **kwargs)

        return wrapper

    return decorator

@rate_limit(max_calls=3, period=60)
def api_request():
    return "Request accepted"

for _ in range(5):
    try:
        print(api_request())
    except RuntimeError as error:
        print(error)