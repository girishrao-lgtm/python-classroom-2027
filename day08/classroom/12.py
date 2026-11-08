'''
Example 12 — Frequency Counting Using Dictionaries
'''
numbers = [4, 2, 4, 3, 2, 4, 5, 3]

frequency = {}

for x in numbers:
    frequency[x] = frequency.get(x, 0) + 1

print(frequency)

for number, count in frequency.items():
    print(number, count)

maximum = max(frequency, key=frequency.get)
print("Most frequent:", maximum)