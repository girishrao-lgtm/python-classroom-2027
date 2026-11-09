'''
Exercise 08 — Custom Dataclass Serialization
'''

import json
from dataclasses import asdict, dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    product_id: int
    name: str
    price: Decimal


def serialize_product(product):
    data = asdict(product)
    data["price"] = str(data["price"])

    return json.dumps(data)


def deserialize_product(text):
    data = json.loads(text)

    return Product(
        product_id=data["product_id"],
        name=data["name"],
        price=Decimal(data["price"])
    )


product = Product(
    101,
    "Laptop",
    Decimal("49999.99")
)

serialized = serialize_product(product)
restored = deserialize_product(serialized)

print(serialized)
print(restored)
print(product == restored)