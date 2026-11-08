'''
Example 20 — Production-Oriented Decorator with Metrics
'''

from functools import wraps
from time import perf_counter


def monitor(func):

    stats = {
        "calls": 0,
        "success": 0,
        "failures": 0,
        "total_time": 0.0
    }

    @wraps(func)
    def wrapper(*args, **kwargs):
        stats["calls"] += 1

        start = perf_counter()

        try:
            result = func(*args, **kwargs)
        except Exception:
            stats["failures"] += 1
            raise
        else:
            stats["success"] += 1
            return result
        finally:
            stats["total_time"] += perf_counter() - start

    wrapper.stats = stats

    return wrapper

@monitor
def process_order(amount):

    if amount <= 0:
        raise ValueError("Invalid amount")

    return amount * 1.18

print(process_order(1000))

try:
    process_order(-100)
except ValueError:
    print("Invalid order")

print(process_order.stats)