'''
Stretch 06 — Detect Duplicate Transaction IDs
'''
transactions = [101, 205, 101, 309, 205, 412, 101]

seen = set()
duplicates = []
reported = set()

for transaction in transactions:

    if transaction in seen and transaction not in reported:
        duplicates.append(transaction)
        reported.add(transaction)

    seen.add(transaction)

print(f"Duplicate IDs: {duplicates}")