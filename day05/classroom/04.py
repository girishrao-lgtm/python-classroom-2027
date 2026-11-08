'''
Classroom 04 — Slicing boundary experiments
Concept: Empty slices, negative boundaries, and invalid step sizes.
'''
text = "ABCDEFGHIJ"

print(text[2:7])
print(text[-5:-1])
print(text[-3:])
print(text[:-3])

print(text[7:2:-1])
print(text[2:7:-1])

print(text[20:30])
print(text[-20:3])

try:
    print(text[::0])
except ValueError as error:
    print(f"Error: {error}")