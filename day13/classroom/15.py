'''
Example 15 — Multiple Context Managers and Cleanup Order
'''
from contextlib import contextmanager


@contextmanager
def resource(name):
    print("Opening:", name)

    try:
        yield name

    finally:
        print("Closing:", name)


with resource("Database") as db, resource("File") as file:
    print("Using:", db, file)