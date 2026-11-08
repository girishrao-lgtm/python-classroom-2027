'''
Exercise 16 — Longest Substring Without Repeating Characters
'''
s = "abcabcbb"

seen = set()
left = 0
best_length = 0
best_start = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    length = right - left + 1

    if length > best_length:
        best_length = length
        best_start = left

print("Length:", best_length)
print("Substring:", s[best_start:best_start + best_length])