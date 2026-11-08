'''
Exercise 19 — Minimum Window Substring
'''
s = "ADOBECODEBANC"
t = "ABC"

need = {}

for ch in t:
    need[ch] = need.get(ch, 0) + 1

window = {}
required = len(need)
formed = 0

left = 0
best_length = float("inf")
best_start = 0

for right, ch in enumerate(s):
    window[ch] = window.get(ch, 0) + 1

    if ch in need and window[ch] == need[ch]:
        formed += 1

    while formed == required:
        length = right - left + 1

        if length < best_length:
            best_length = length
            best_start = left

        outgoing = s[left]
        window[outgoing] -= 1

        if outgoing in need and window[outgoing] < need[outgoing]:
            formed -= 1

        left += 1

if best_length == float("inf"):
    print()
else:
    print(s[best_start:best_start + best_length])
