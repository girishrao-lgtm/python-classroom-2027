'''
Stretch 19 — Duplicate Transaction Detector
Given a list of transaction IDs, identify each duplicated ID once, without using sets or dictionaries.
'''
transactions = [101, 205, 101, 309, 205, 101, 412]

n = len(transactions)

print("Duplicate transaction IDs:")

for i in range(n):

    already_seen = False

    for k in range(i):

        if transactions[k] == transactions[i]:
            already_seen = True
            break

    if already_seen:
        continue

    count = 0

    for j in range(n):

        if transactions[i] == transactions[j]:
            count += 1

    if count > 1:
        print(f"{transactions[i]} occurs {count} times")
        