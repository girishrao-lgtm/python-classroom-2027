'''
Exercise 06 — Unique Customer Registration
'''
registrations = [101, 102, 103, 101, 104, 102, 105]

seen = set()
unique_customers = []

for customer in registrations:
    if customer not in seen:
        seen.add(customer)
        unique_customers.append(customer)

print("Unique registrations:", unique_customers)
print("Total unique:", len(seen))
print("Duplicates:", len(registrations) - len(seen))