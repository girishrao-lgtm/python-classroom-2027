'''
Classroom 20 — Longest substring without repeating characters
Concept: Sliding window and tracking the last-seen index.
'''

text = input("Enter string: ")

last_seen = {}

left = 0
max_length = 0
best_start = 0

for right in range(len(text)):

    ch = text[right]

    if ch in last_seen and last_seen[ch] >= left:
        left = last_seen[ch] + 1

    last_seen[ch] = right

    current_length = right - left + 1

    if current_length > max_length:
        max_length = current_length
        best_start = left

longest = text[best_start:best_start + max_length]

print(f"Longest substring = {longest}")
print(f"Length = {max_length}")