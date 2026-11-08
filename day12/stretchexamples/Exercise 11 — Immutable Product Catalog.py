'''
Exercise 11 — Immutable Product Catalog
'''

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Product:
    product_id: int
    name: str
    price: float


products = (
    Product(101, "Laptop", 50000),
    Product(102, "Mouse", 500),
    Product(103, "Keyboard", 1500)
)

updated_product = replace(
    products[0],
    price=48000
)

updated_catalog = (
    updated_product,
    *products[1:]
)

print(products)
print(updated_catalog)