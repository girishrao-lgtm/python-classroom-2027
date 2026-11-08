'''
Stretch 04 — Rotate a String by K Positions
Given a string and integer K, rotate the string to the right by K positions.

Example: abcdef, K = 2 produces efabcd
'''

text = input("Enter string: ")
k = int(input("Enter rotation count: "))

n = len(text)

if n == 0:
    print("Rotated string = ")
else:
    k %= n

    if k == 0:
        rotated = text
    else:
        rotated = text[-k:] + text[:-k]

    print(f"Rotated string = {rotated}")