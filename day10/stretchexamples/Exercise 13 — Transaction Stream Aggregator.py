'''
Exercise 13 — Transaction Stream Aggregator
'''

def transaction_stream():
    transactions = [
        ("C101", 500),
        ("C102", 1000),
        ("C101", 700),
        ("C103", 300),
        ("C102", 200)
    ]

    yield from transactions


def aggregate_transactions(transactions):
    totals = {}

    for customer, amount in transactions:
        totals[customer] = totals.get(customer, 0) + amount
        yield customer, totals[customer]


for result in aggregate_transactions(transaction_stream()):
    print(result)
    