'''
Example 17 — Set Mutability and Frozensets
'''

a = {10, 20, 30}

a.add(40)
print(a)

b = frozenset([10, 20, 30, 20])
print(b)
print(hash(b))

try:
    b.add(40)
except AttributeError:
    print("Frozenset cannot be modified")

nested = {
    frozenset({1, 2}),
    frozenset({2, 3})
}

print(nested)

print(frozenset({1, 2}) in nested)
