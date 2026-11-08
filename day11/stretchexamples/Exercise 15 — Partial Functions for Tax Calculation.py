'''
Exercise 15 — Partial Functions for Tax Calculation
'''

from functools import partial


def calculate_total(price, tax, discount):
    return price * (1 + tax) * (1 - discount)

gst_5 = partial(calculate_total, tax=0.05)
gst_18 = partial(calculate_total, tax=0.18)

student_gst_18 = partial(gst_18, discount=0.10)

print(gst_5(1000, discount=0))
print(gst_18(1000, discount=0))
print(student_gst_18(1000))
