'''
Example 05 — Constructor and Object Lifecycle
'''
class Resource:

    def __new__(cls, name):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self, name):
        print("__init__ called")
        self.name = name

    def __del__(self):
        print("Object finalizer called")


resource = Resource("Database Connection")

print(resource.name)

del resource

print("Reference deleted")