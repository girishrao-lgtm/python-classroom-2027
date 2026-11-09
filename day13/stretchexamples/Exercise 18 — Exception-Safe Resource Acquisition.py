'''
Exercise 18 — Exception-Safe Resource Acquisition
'''
from contextlib import ExitStack, contextmanager


@contextmanager
def acquire_resource(name):
    print("Acquiring:", name)

    try:
        yield name

    finally:
        print("Releasing:", name)


def initialize_system():
    with ExitStack() as stack:
        database = stack.enter_context(
            acquire_resource("Database")
        )

        cache = stack.enter_context(
            acquire_resource("Cache")
        )

        print("Resources:", database, cache)

        raise RuntimeError("Initialization failed")


try:
    initialize_system()

except RuntimeError as error:
    print(error)