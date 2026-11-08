'''
Example 20 — Streaming Data Processing Pipeline
'''

def read_transactions():
    transactions = [
        ("T101", 500),
        ("T102", -100),
        ("T103", 1200),
        ("T104", 700),
        ("T105", -50),
        ("T106", 2000)
    ]

    for transaction in transactions:
        yield transaction


def valid_transactions(transactions):
    for transaction_id, amount in transactions:
        if amount > 0:
            yield transaction_id, amount


def high_value_transactions(transactions, threshold):
    for transaction_id, amount in transactions:
        if amount >= threshold:
            yield transaction_id, amount


def calculate_total(transactions):
    total = 0

    for transaction_id, amount in transactions:
        print("Processing:", transaction_id, amount)
        total += amount

    return total


pipeline = high_value_transactions(
    valid_transactions(read_transactions()),
    threshold=1000
)

print("Total:", calculate_total(pipeline))