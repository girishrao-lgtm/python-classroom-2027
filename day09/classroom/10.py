'''
Example 10 — Local, Global and Nonlocal Scope: LEGB
'''
value = "Global"


def outer():
    value = "Enclosing"

    def inner():
        value = "Local"
        print("Inner:", value)

    inner()
    print("Outer:", value)


outer()
print("Global:", value)


counter = 10


def update_global():
    global counter
    counter += 5


update_global()
print("Global counter:", counter)


def enclosing():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    print(increment())
    print(increment())


enclosing()