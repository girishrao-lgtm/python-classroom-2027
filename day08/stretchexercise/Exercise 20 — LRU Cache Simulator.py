'''
Exercise 20 — LRU Cache Simulator
'''

from collections import OrderedDict

capacity = 2
cache = OrderedDict()

operations = [
    ("PUT", 1, 10),
    ("PUT", 2, 20),
    ("GET", 1),
    ("PUT", 3, 30),
    ("GET", 2),
    ("PUT", 4, 40),
    ("GET", 1),
    ("GET", 3),
    ("GET", 4)
]

for operation in operations:
    command = operation[0]

    if command == "GET":
        key = operation[1]

        if key not in cache:
            print(-1)
        else:
            cache.move_to_end(key)
            print(cache[key])

    elif command == "PUT":
        key, value = operation[1], operation[2]

        if capacity == 0:
            continue

        if key in cache:
            cache.move_to_end(key)

        cache[key] = value

        if len(cache) > capacity:
            cache.popitem(last=False)

print("Final cache:", dict(cache))