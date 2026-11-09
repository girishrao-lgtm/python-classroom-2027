'''
Example 06 — Raising Exceptions Explicitly
'''
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount


requests = [200, -100, 1500]

for amount in requests:
    try:
        print(withdraw(1000, amount))

    except ValueError as error:
        print(error)
        