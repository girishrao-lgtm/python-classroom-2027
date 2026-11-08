'''
Exercise 14 — Functional Data Processing Pipeline
'''

from functools import reduce

transactions = [
    {"type": "credit", "amount": 1000},
    {"type": "debit", "amount": 300},
    {"type": "credit", "amount": 2000},
    {"type": "credit", "amount": 500}
]

credits = filter(
    lambda transaction: transaction["type"] == "credit",
    transactions
)

amounts = (transaction["amount"] for transaction in credits)

total = reduce(
    lambda a, b: a + b,
    amounts,
    0
)

print("Total credits:", total)