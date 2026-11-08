'''
Exercise 04 — First Non-Repeating Character
'''

s = "aabbcddeff"

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

answer = -1

for i, ch in enumerate(s):
    if frequency[ch] == 1:
        answer = i
        break

print("Index:", answer)
print("Character:", s[answer] if answer != -1 else None)