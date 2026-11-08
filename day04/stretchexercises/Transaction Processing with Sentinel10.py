'''
Stretch 10 — Transaction Processing with Sentinel
Accept transaction amounts until zero is entered. Ignore negative transactions.

'''
total = 0
valid_transactions = 0
invalid_transactions = 0

while True:

    amount = float(input("Enter transaction (0 to stop): "))

    if amount == 0:
        break

    if amount < 0:
        invalid_transactions += 1
        continue

    total += amount
    valid_transactions += 1

print(f"Valid transactions = {valid_transactions}")
print(f"Invalid transactions = {invalid_transactions}")
print(f"Total amount = {total:.2f}")