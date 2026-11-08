'''
Exercise 08 — Merge Warehouse Inventories
'''

warehouse_a = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15
}

warehouse_b = {
    "Laptop": 5,
    "Mouse": 12,
    "Monitor": 8
}

combined = warehouse_a.copy()

for item, quantity in warehouse_b.items():
    combined[item] = combined.get(item, 0) + quantity

print(combined)