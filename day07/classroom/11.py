'''
Example 11 — Set Creation and Basic Operations
'''
a = set()
b = {10, 20, 30, 20, 10}  # noqa: B033
c = {1, 2, 2, 3, 3, 4}  # noqa: B033
d = set("BANANA")

print(type(a))
print(b)
print(c)
print(d)

print(len(b))
print(20 in b)

try:
    print(b[0])
except TypeError:
    print("Sets do not support indexing")