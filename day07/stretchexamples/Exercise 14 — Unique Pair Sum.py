'''
Exercise 14 — Unique Pair Sum
'''
numbers = [1, 5, 7, -1, 5, 3, 3, 4, 2]
target = 6

seen = set()
pairs = set()

for x in numbers:
    complement = target - x

    if complement in seen:
        pair = (min(x, complement), max(x, complement))
        pairs.add(pair)

    seen.add(x)

print("Unique pairs:", sorted(pairs))
print("Count:", len(pairs))
