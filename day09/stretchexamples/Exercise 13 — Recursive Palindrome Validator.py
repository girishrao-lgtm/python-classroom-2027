'''
Exercise 13 — Recursive Palindrome Validator
'''

def is_palindrome(s, left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return is_palindrome(s, left + 1, right - 1)


words = ["madam", "racecar", "python", "level"]

for word in words:
    print(word, is_palindrome(word, 0, len(word) - 1))
    