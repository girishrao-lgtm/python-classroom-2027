'''
Exercise 10 — Temporary Environment Variables
'''
import os
from contextlib import contextmanager


@contextmanager
def temporary_environment(key, value):  
    existed = key in os.environ
    old_value = os.environ.get(key)

    os.environ[key] = value

    try:
        yield

    finally:
        if existed:
            os.environ[key] = old_value
        else:
            os.environ.pop(key, None)


print("Before:", os.getenv("APP_MODE"))

with temporary_environment("APP_MODE", "testing"):
    print("Inside:", os.getenv("APP_MODE"))

print("After:", os.getenv("APP_MODE"))