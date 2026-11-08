'''
Exercise 18 — Merge Two Sorted Streams
'''

def merge_sorted(stream1, stream2):
    a = iter(stream1)
    b = iter(stream2)

    sentinel = object()

    x = next(a, sentinel)
    y = next(b, sentinel)

    while x is not sentinel and y is not sentinel:
        if x <= y:
            yield x
            x = next(a, sentinel)
        else:
            yield y
            y = next(b, sentinel)

    while x is not sentinel:
        yield x
        x = next(a, sentinel)

    while y is not sentinel:
        yield y
        y = next(b, sentinel)


a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]

print(list(merge_sorted(a, b)))