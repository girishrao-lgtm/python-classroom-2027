'''
Example 05 — Tuple Methods and Membership
'''
t = (10, 20, 10, 30, 10, 40)

print(t.count(10))
print(t.index(30))
print(t.index(10, 2))

print(20 in t)
print(50 not in t)

try:
    print(t.index(100))
except ValueError:
    print("Element not found")