'''
Example 14 — Union, Intersection, Difference and Symmetric Difference
'''
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("Union:", a | b)
print("Intersection:", a & b)
print("A - B:", a - b)
print("B - A:", b - a)
print("Symmetric Difference:", a ^ b)

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))