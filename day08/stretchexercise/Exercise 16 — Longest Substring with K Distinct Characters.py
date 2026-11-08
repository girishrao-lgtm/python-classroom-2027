'''
Exercise 16 — Longest Substring with K Distinct Characters
'''

s = "aabacbebebe"
k = 3

frequency = {}
left = 0
longest = 0
best_start = 0

for right, ch in enumerate(s):
    frequency[ch] = frequency.get(ch, 0) + 1

    while len(frequency) > k:
        outgoing = s[left]
        frequency[outgoing] -= 1

        if frequency[outgoing] == 0:
            del frequency[outgoing]

        left += 1

    if len(frequency) == k:
        length = right - left + 1

        if length > longest:
            longest = length
            best_start = left

print("Length:", longest)
print("Substring:", s[best_start:best_start + longest])

