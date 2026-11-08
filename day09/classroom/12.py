'''
Example 12 — Mutable Default Argument Pitfall
'''

def incorrect_add(value, items=[]):
    items.append(value)
    return items


print(incorrect_add(10))
print(incorrect_add(20))
print(incorrect_add(30))


def correct_add(value, items=None):
    if items is None:
        items = []

    items.append(value)
    return items


print(correct_add(10))
print(correct_add(20))
print(correct_add(30))