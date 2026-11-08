'''
Exercise 20 — Complete Decorator-Based API Processing Pipeline
'''

from functools import wraps
from time import perf_counter


def authenticate(func):

    @wraps(func)
    def wrapper(user, *args, **kwargs):

        if not user.get("authenticated", False):
            raise PermissionError("Authentication required")

        return func(user, *args, **kwargs)

    return wrapper

def validate_amount(func):

    @wraps(func)
    def wrapper(user, amount):

        if type(amount) not in (int, float) or amount <= 0:
            raise ValueError("Invalid amount")

        return func(user, amount)

    return wrapper

def measure_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            print(
                f"Execution time: "
                f"{perf_counter() - start:.6f}s"
            )

    return wrapper

def log_request(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print("Request started")

        try:
            result = func(*args, **kwargs)
        except Exception as error:
            print("Request failed:", type(error).__name__)
            raise

        print("Request completed")
        return result

    return wrapper

@log_request
@measure_time
@authenticate
@validate_amount
def process_payment(user, amount):

    return {
        "user": user["name"],
        "amount": amount,
        "status": "SUCCESS"
    }

user = {
    "name": "Alice",
    "authenticated": True
}

print(process_payment(user, 2500))

try:
    print(process_payment(user, -100))
except ValueError as error:
    print(error)