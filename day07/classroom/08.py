'''
Example 08 — Tuple Hashability and Dictionary Keys
'''
a = (10, 20, 30)
print(hash(a))

locations = {}

locations[(10, 20)] = "Warehouse A"
locations[(15, 25)] = "Warehouse B"

print(locations)
print(locations[(10, 20)])

b = (10, [20, 30])

try:
    print(hash(b))
except TypeError as e:
    print(type(e).__name__, e)

print("Tuple hashability depends on its elements")
