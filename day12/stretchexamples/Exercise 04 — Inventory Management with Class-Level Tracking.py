'''
Exercise 04 — Inventory Management with Class-Level Tracking
'''
class Product:

    total_products = 0

    def __init__(self, product_id, name, quantity):
        if quantity < 0:
            raise ValueError("Invalid quantity")

        self.product_id = product_id
        self.name = name
        self.quantity = quantity

        Product.total_products += 1

    def restock(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        self.quantity += quantity

    def sell(self, quantity):
        if quantity <= 0 or quantity > self.quantity:
            raise ValueError("Insufficient stock")

        self.quantity -= quantity


products = [
    Product(101, "Laptop", 10),
    Product(102, "Mouse", 50)
]

products[0].sell(3)
products[1].restock(20)

for product in products:
    print(product.name, product.quantity)

print(Product.total_products)

