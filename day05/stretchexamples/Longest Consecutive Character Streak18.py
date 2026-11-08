'''
Stretch 18 — Longest Consecutive Character Streak
Find the character with the longest consecutive run.

Example: aabbbbbccaaa produces b, length 5.
'''

text = input("Enter string: ")

if not text:
    print("Empty string")

else:
    best_char = text[0]
    max_length = 1
    current_length = 1

    for i in range(1, len(text)):

        if text[i] == text[i - 1]:
            current_length += 1

        else:
            current_length = 1

        if current_length > max_length:
            max_length = current_length
            best_char = text[i]

    print(f"Character = {best_char}")
    print(f"Longest streak = {max_length}")