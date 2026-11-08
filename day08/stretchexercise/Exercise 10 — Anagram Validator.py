'''
Exercise 10 — Anagram Validator
'''

s = "listen"
t = "silent"

if len(s) != len(t):
    print(False)
else:
    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in t:
        frequency[ch] = frequency.get(ch, 0) - 1

    print(all(count == 0 for count in frequency.values()))
    