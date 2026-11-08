'''
Exercise 02 — Flexible Shopping Bill Calculator
'''

def calculate_bill(price, quantity=1, discount=0, tax=18):
    subtotal = price * quantity
    discounted = subtotal * (1 - discount / 100)
    final_amount = discounted * (1 + tax / 100)

    return round(final_amount, 2)


print(calculate_bill(1000))
print(calculate_bill(1000, 3))
print(calculate_bill(1000, 3, discount=10))
print(calculate_bill(1000, quantity=2, tax=5))