'''

Classroom 03 — Slicing with start, stop, and step
Concept: text[start:stop:step], exclusive stop, and negative steps.
'''

text = "PythonProgramming"

print(text[0:6])
print(text[6:])
print(text[:6])
print(text[::2])
print(text[1::2])
print(text[::-1])
print(text[5:1:-1])

print(text[:])
print(text[100:200])

print(f"Length = {len(text)}")