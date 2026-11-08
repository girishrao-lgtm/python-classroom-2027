'''
Example 07 — Properties and Validation
'''

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")

        self._price = value


product = Product("Laptop", 50000)

print(product.price)

product.price = 55000

print(product.price)

try:
    product.price = -100
except ValueError as error:
    print(error)
    