'''
Example 04 — Tuple Immutability and Mutable Elements
'''
t = (10, 20, 30)

print(id(t))

try:
    t[0] = 100
except TypeError as e:
    print(type(e).__name__, e)

data = (10, [20, 30], 40)

print(data)
print(id(data))
print(id(data[1]))

data[1].append(50)
data[1][0] = 200

print(data)
print(id(data))
print(id(data[1]))