'''
Exercise 05 — Most Frequent Element
'''

numbers = [4, 2, 4, 3, 2, 4, 3, 3]

frequency = {}

for x in numbers:
    frequency[x] = frequency.get(x, 0) + 1

maximum = max(frequency.values())

candidates = [
    x for x, count in frequency.items()
    if count == maximum
]

answer = min(candidates)

print("Element:", answer)
print("Frequency:", maximum)
