'''
Stretch 09 — First Non-Repeating Character
Given a string, find the first character that occurs exactly once. Preserve case sensitivity.
'''

text = input("Enter string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

found = False

for index, ch in enumerate(text):

    if frequency[ch] == 1:
        print(f"Character = {ch}")
        print(f"Index = {index}")
        found = True
        break

if not found:
    print("No non-repeating character")