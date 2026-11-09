'''
Exercise 19 — Transactional Order Processing
'''

from contextlib import contextmanager
from copy import deepcopy

inventory = {
    "Laptop": 10,
    "Mouse": 50
}

orders = []


@contextmanager
def transaction():
    inventory_snapshot = deepcopy(inventory)
    orders_snapshot = deepcopy(orders)

    try:
        yield

    except Exception:
        inventory.clear()
        inventory.update(inventory_snapshot)

        orders.clear()
        orders.extend(orders_snapshot)

        raise


def place_order(product, quantity):
    with transaction():
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if product not in inventory:
            raise KeyError("Unknown product")

        if inventory[product] < quantity:
            raise ValueError("Insufficient stock")

        inventory[product] -= quantity

        orders.append({
            "product": product,
            "quantity": quantity
        })


place_order("Laptop", 2)

try:
    place_order("Mouse", 100)

except ValueError as error:
    print(error)

print(inventory)
print(orders)