'''
Exercise 09 — Product Filtering Pipeline
'''

from functools import reduce

products = [
    ("Laptop", 60000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Headphones", 2500)
]

filtered = list(
    filter(lambda product: product[1] >= 2000, products)
)

discounted = [(product[0], product[1] * 0.9) for product in filtered]

total = reduce(
    lambda amount, product: amount + product[1],
    discounted,
    0
)

print(filtered)
print(discounted)
print("Total:", total)