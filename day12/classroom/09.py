'''
Example 09 — Custom Descriptor for Attribute Validation
'''
class PositiveNumber:

    def __set_name__(self, owner, name):
        self.storage_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Value must be positive")

        setattr(instance, self.storage_name, value)


class Product:

    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity


product = Product(100, 5)

print(product.price)
print(product.quantity)

product.quantity = 10

print(product.__dict__)

try:
    product.price = -50
except ValueError as error:
    print(error)