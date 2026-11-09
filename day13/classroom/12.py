'''
Example 12 — Context Manager Protocol: __enter__ and __exit__
'''
class ResourceManager:

    def __enter__(self):
        print("Resource acquired")
        return self

    def process(self):
        print("Processing resource")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")

        if exc_type is not None:
            print("Exception:", exc_type.__name__)

        return False


with ResourceManager() as resource:
    resource.process()