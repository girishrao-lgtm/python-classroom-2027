'''
Stretch 06 — Discount Eligibility Scanner
A store offers discounts on purchases of at least ₹5,000. Read N purchases and count eligible customers.
'''
n = int(input("Number of customers: "))

eligible = 0
total_eligible_amount = 0

for customer in range(1, n + 1):

    amount = float(input(f"Customer {customer} purchase: "))

    if amount < 5000:
        continue

    eligible += 1
    total_eligible_amount += amount

print(f"Eligible customers = {eligible}")
print(f"Eligible purchase total = {total_eligible_amount:.2f}")