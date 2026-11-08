'''
Stretch 05 — Even Number Revenue Filter
A system records transaction IDs from 1 to N. Calculate the sum of IDs that are even and divisible by 3.

'''
n = int(input("Enter N: "))

total = 0

for transaction_id in range(1, n + 1):

    if transaction_id % 2 == 0 and transaction_id % 3 == 0:
        print(transaction_id)
        total += transaction_id

print(f"Total = {total}")