'''
Example 13 — Set Membership and Deduplication
'''
numbers = [10, 20, 10, 30, 20, 40, 50, 30]

unique = set(numbers)

print("Original:", numbers)
print("Unique:", unique)
print("Distinct count:", len(unique))

seen = set()
ordered_unique = []

for x in numbers:
    if x not in seen:
        seen.add(x)
        ordered_unique.append(x)

print("First-occurrence order:", ordered_unique)