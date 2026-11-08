'''
Example 20 — Longest Consecutive Sequence
'''
numbers = [100, 4, 200, 1, 3, 2, 5, 5]

values = set(numbers)

longest = 0
best_start = None

for x in values:
    if x - 1 not in values:
        current = x
        length = 0

        while current in values:
            length += 1
            current += 1

        if length > longest:
            longest = length
            best_start = x

print("Longest length:", longest)

if best_start is not None:
    sequence = tuple(range(best_start, best_start + longest))
    print("Sequence:", sequence)