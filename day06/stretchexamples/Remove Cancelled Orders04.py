'''
Stretch 04 — Remove Cancelled Orders
'''
orders = [101, 102, 103, 104, 105, 106]
cancelled = [102, 105]

active_orders = []

for order in orders:

    if order not in cancelled:
        active_orders.append(order)

print(f"Active orders: {active_orders}")