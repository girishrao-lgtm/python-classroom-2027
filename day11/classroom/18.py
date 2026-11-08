'''
Example 18 — Partial Functions
'''

from functools import partial


def calculate_price(price, tax_rate, discount):
    return price * (1 + tax_rate) * (1 - discount)

gst_price = partial(
    calculate_price,
    tax_rate=0.18
)

student_price = partial(
    gst_price,
    discount=0.10
)

print(gst_price(1000, discount=0))
print(student_price(1000))
