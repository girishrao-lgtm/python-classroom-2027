'''
Example 20 — LRU Cache Using OrderedDict
'''
from collections import OrderedDict

capacity = 3
cache = OrderedDict()

operations = [
    ("PUT", 1, 100),
    ("PUT", 2, 200),
    ("PUT", 3, 300),
    ("GET", 1),
    ("PUT", 4, 400),
    ("GET", 2),
    ("GET", 3)
]

for operation in operations:
    if operation[0] == "PUT":
        key, value = operation[1], operation[2]

        if key in cache:
            cache.move_to_end(key)

        cache[key] = value

        if len(cache) > capacity:
            cache.popitem(last=False)

    elif operation[0] == "GET":
        key = operation[1]

        if key in cache:
            cache.move_to_end(key)
            print(cache[key])
        else:
            print(-1)

    print(dict(cache))