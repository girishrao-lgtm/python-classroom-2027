'''
Exercise 10 — Duplicate Transaction Detector
'''
transactions = [501, 502, 503, 501, 504, 502, 505]

seen = set()
duplicates = set()

for transaction in transactions:
    if transaction in seen:
        duplicates.add(transaction)
    else:
        seen.add(transaction)

print("Duplicate transaction IDs:", sorted(duplicates))
print("Duplicate ID count:", len(duplicates))
