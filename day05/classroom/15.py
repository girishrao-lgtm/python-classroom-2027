'''

Classroom 15 — Palindrome ignoring spaces and punctuation
Concept: Normalization and two-pointer traversal.
'''
text = input("Enter sentence: ")

left = 0
right = len(text) - 1

is_palindrome = True

while left < right:

    if not text[left].isalnum():
        left += 1
        continue

    if not text[right].isalnum():
        right -= 1
        continue

    if text[left].casefold() != text[right].casefold():
        is_palindrome = False
        break

    left += 1
    right -= 1

print("Palindrome" if is_palindrome else "Not palindrome")