'''
Classroom 14 — Palindrome checking using two pointers
Concept: Comparing symmetric positions.
'''

text = input("Enter text: ")

left = 0
right = len(text) - 1

is_palindrome = True

while left < right:

    if text[left] != text[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")