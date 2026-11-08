'''
Example 02 — Dictionary Keys and Hashability
'''
data = {
    101: "Integer Key",
    "name": "String Key",
    (10, 20): "Tuple Key",
    3.14: "Float Key",
    True: "Boolean Key"
}

for key, value in data.items():
    print(key, value)

print(hash("Python"))
print(hash((10, 20)))

try:
    data[[1, 2]] = "List Key"
except TypeError as e:
    print(type(e).__name__, e)

try:
    data[{1, 2}] = "Set Key"
except TypeError as e:
    print(type(e).__name__, e)