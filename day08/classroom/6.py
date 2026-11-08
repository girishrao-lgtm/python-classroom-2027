'''
Example 06 — Dictionary Insertion Order
'''

data = {}

data["A"] = 10
data["B"] = 20
data["C"] = 30

print(data)

data["B"] = 200
print(data)

del data["A"]
data["A"] = 100

print(data)

for key, value in data.items():
    print(key, value)