'''
Stretch 10 — Most Frequent Character
Find the most frequently occurring character. If multiple characters have the same maximum frequency, choose the one appearing first.

'''

text = input("Enter string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

max_count = 0
result = None

for ch in text:

    if frequency[ch] > max_count:
        max_count = frequency[ch]
        result = ch

if result is None:
    print("Empty string")
else:
    print(f"Most frequent character = {repr(result)}")
    print(f"Frequency = {max_count}")