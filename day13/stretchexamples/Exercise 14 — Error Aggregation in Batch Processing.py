'''
Exercise 14 — Error Aggregation in Batch Processing
'''

def process_record(record):
    if "amount" not in record:
        raise KeyError("Missing amount")

    amount = record["amount"]

    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be numeric")

    if amount <= 0:
        raise ValueError("Amount must be positive")

    return amount * 1.18


records = [
    {"amount": 100},
    {"amount": -50},
    {},
    {"amount": "abc"},
    {"amount": 200}
]

results = []
errors = []

for index, record in enumerate(records):
    try:
        results.append(process_record(record))

    except (KeyError, TypeError, ValueError) as error:
        errors.append({
            "index": index,
            "error": str(error)
        })


print("Results:", results)
print("Errors:", errors)