'''
Example 13 — Character Frequency and First Non-Repeating Character
'''
s = "programming"

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)

answer = None

for ch in s:
    if frequency[ch] == 1:
        answer = ch
        break

print("First non-repeating:", answer)
