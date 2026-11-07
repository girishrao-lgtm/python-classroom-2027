balance = 15000
daily_limit = 10000

amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount % 100 != 0:
    print("Amount must be a multiple of 100")
elif amount > daily_limit:
    print("Daily limit exceeded")
elif amount > balance:
    print("Insufficient balance")
else:
    balance -= amount
    print("Withdrawal successful")
    print(f"Remaining balance: {balance}")