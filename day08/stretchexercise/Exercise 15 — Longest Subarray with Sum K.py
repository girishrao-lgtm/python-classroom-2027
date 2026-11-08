'''
Exercise 15 — Longest Subarray with Sum K
'''

numbers = [10, 5, 2, 7, 1, 9]
k = 15

prefix = 0
first_index = {0: -1}

longest = 0
best = None

for i, x in enumerate(numbers):
    prefix += x

    if prefix - k in first_index:
        start = first_index[prefix - k] + 1
        length = i - start + 1

        if length > longest:
            longest = length
            best = (start, i)

    if prefix not in first_index:
        first_index[prefix] = i

print("Longest length:", longest)
print("Indices:", best)
