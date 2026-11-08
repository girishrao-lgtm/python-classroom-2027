'''
Exercise 13 — Immutable Shopping Cart
'''

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Cart:
    items: tuple

def add_item(cart, item):
    return replace(
        cart,
        items=cart.items + (item,)
    )

def remove_item(cart, item):

    items = list(cart.items)
    items.remove(item)

    return replace(
        cart,
        items=tuple(items)
    )

cart1 = Cart(("Laptop",))

cart2 = add_item(cart1, "Mouse")
cart3 = add_item(cart2, "Keyboard")
cart4 = remove_item(cart3, "Mouse")

print(cart1)
print(cart2)
print(cart3)
print(cart4)