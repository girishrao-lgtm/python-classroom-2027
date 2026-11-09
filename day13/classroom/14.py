'''
Example 14 — Generator-Based Context Manager
'''
from contextlib import contextmanager


@contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")

    try:
        yield name

    finally:
        print(f"Releasing {name}")


with managed_resource("Database") as resource:
    print("Using:", resource)