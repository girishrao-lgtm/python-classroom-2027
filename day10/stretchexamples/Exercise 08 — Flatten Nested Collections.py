'''
Exercise 08 — Flatten Nested Collections
'''

def flatten(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item


data = [
    1,
    [2, 3],
    (4, [5, 6]),
    [7, [8, 9]]
]

print(list(flatten(data)))