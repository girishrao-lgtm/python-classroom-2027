'''
Exercise 08 — Resource Pool Context Manager
'''
from contextlib import contextmanager


class ResourcePool:

    def __init__(self, size):
        self.available = [
            f"Connection-{i}"
            for i in range(1, size + 1)
        ]

    @contextmanager
    def acquire(self):
        if not self.available:
            raise RuntimeError("No resources available")

        resource = self.available.pop()

        try:
            yield resource

        finally:
            self.available.append(resource)


pool = ResourcePool(2)

with pool.acquire() as connection1:
    print("Using:", connection1)

    with pool.acquire() as connection2:
        print("Using:", connection2)

print("Available:", pool.available)
