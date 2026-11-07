'''
ATM Withdrawal with Minimum Balance
Difficulty: Medium

An ATM account has a balance of ₹20,000. The customer must maintain a minimum balance of ₹1,000 after withdrawal. Withdrawals must be positive multiples of ₹100 and cannot exceed ₹10,000 per transaction.

Input: Withdrawal amount.

Output: SUCCESS followed by remaining balance on a new line, or one of INVALID AMOUNT, LIMIT EXCEEDED, INSUFFICIENT FUNDS.

'''
balance = 20000
minimum_balance = 1000
transaction_limit = 10000

amount = int(input())

if amount <= 0 or amount % 100 != 0:
    print("INVALID AMOUNT")
elif amount > transaction_limit:
    print("LIMIT EXCEEDED")
elif balance - amount < minimum_balance:
    print("INSUFFICIENT FUNDS")
else:
    balance -= amount
    print("SUCCESS")
    print(balance)