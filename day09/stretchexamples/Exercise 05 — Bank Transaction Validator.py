'''
Exercise 05 — Bank Transaction Validator
'''
def withdraw(balance, amount, daily_limit=10000):
    if amount <= 0:
        return False, balance, "Invalid amount"

    if amount > daily_limit:
        return False, balance, "Daily limit exceeded"

    if amount > balance:
        return False, balance, "Insufficient balance"

    balance -= amount

    return True, balance, "Withdrawal successful"


balance = 15000

transactions = [3000, 12000, 5000, -100]

for amount in transactions:
    success, balance, message = withdraw(balance, amount)

    print(amount, success, balance, message)