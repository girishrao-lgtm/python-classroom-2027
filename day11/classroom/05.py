'''
Example 05 — Stateful Closures Using nonlocal
'''

def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter1 = create_counter()
counter2 = create_counter()

print(counter1())
print(counter1())
print(counter1())

print(counter2())
print(counter2())