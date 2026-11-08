'''
Stretch 14 — Detect Anagram Usernames
Two usernames are considered equivalent if they contain the same letters with the same frequencies, ignoring spaces and case.
'''

first = input("Enter first username: ")
second = input("Enter second username: ")

first = "".join(first.casefold().split())
second = "".join(second.casefold().split())

frequency = {}

for ch in first:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in second:
    frequency[ch] = frequency.get(ch, 0) - 1

is_anagram = True

for count in frequency.values():

    if count != 0:
        is_anagram = False
        break

print("Equivalent" if is_anagram else "Not equivalent")