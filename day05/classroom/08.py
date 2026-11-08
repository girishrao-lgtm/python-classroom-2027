'''
Classroom 08 — Traversal with for, while, and enumerate()
Concept: Three ways to traverse a string.
'''
text = "Python"

print("Using for:")

for ch in text:
    print(ch)

print("Using while:")

i = 0

while i < len(text):
    print(text[i])
    i += 1

print("Using enumerate:")

for index, ch in enumerate(text):
    print(f"{index}: {ch}")