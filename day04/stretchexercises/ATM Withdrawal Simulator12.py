'''
Stretch 12 — ATM Withdrawal Simulator
An ATM starts with a fixed balance. Process withdrawals until the user enters zero. Reject invalid withdrawals.
'''
balance = 10000

while True:

    print(f"\nAvailable balance: {balance}")

    amount = int(input("Withdrawal amount (0 to exit): "))

    if amount == 0:
        print("Session ended")
        break

    if amount < 0:
        print("Invalid amount")
        continue

    if amount > balance:
        print("Insufficient balance")
        continue

    balance -= amount

    print(f"Withdrawal successful: {amount}")

print(f"Final balance = {balance}")