'''
Example 11 — yield from and Generator Delegation
'''

def first_group():
    yield 10
    yield 20
    yield 30


def second_group():
    yield 40
    yield 50


def combined():
    yield from first_group()
    yield from second_group()
    yield 60


print(list(combined()))


def flatten(nested):
    for group in nested:
        yield from group


data = [[1, 2], [3, 4, 5], [6]]

print(list(flatten(data)))