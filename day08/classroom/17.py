'''
Example 17 — Merging Dictionaries and Conflict Resolution
'''
a = {"A": 10, "B": 20}
b = {"B": 200, "C": 30}

merged = a | b
print(merged)

a.update(b)
print(a)

x = {"A": 10, "B": 20}
y = {"B": 5, "C": 30}

combined = x.copy()

for key, value in y.items():
    combined[key] = combined.get(key, 0) + value

print(combined)