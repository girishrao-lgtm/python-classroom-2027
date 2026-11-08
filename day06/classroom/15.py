'''
Classroom 15 — Remove Duplicates While Preserving Order
'''

numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []
seen = set()

for number in numbers:

    if number not in seen:
        seen.add(number)
        unique.append(number)

print(f"Original: {numbers}")
print(f"Unique: {unique}")

