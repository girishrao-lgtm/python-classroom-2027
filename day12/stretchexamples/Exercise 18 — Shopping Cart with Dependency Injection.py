'''
Exercise 18 — Shopping Cart with Dependency Injection
'''
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    price: float


class DiscountStrategy:

    def apply(self, total):
        return total


class PercentageDiscount(DiscountStrategy):

    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, total):
        return total * (1 - self.percentage / 100)


class ShoppingCart:

    def __init__(self, discount_strategy):
        self.items = []
        self.discount_strategy = discount_strategy

    def add_item(self, product):
        self.items.append(product)

    def calculate_total(self):
        total = sum(product.price for product in self.items)
        return self.discount_strategy.apply(total)


cart = ShoppingCart(PercentageDiscount(10))

cart.add_item(Product("Laptop", 50000))
cart.add_item(Product("Mouse", 1000))

print(cart.calculate_total())