'''
Exercise 02 — Inventory Stock Updates
'''
inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

transactions = [
    ("Laptop", -3),
    ("Mouse", 10),
    ("Keyboard", -20),
    ("Monitor", 5)
]

for item, change in transactions:
    current = inventory.get(item, 0)

    if current + change < 0:
        print("Insufficient stock:", item)
    else:
        inventory[item] = current + change

print(inventory)