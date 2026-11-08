'''
Classroom 06 — Concatenation, repetition, and join()
Concept: Creating strings through different operations.
'''

first = "Python"
second = "Programming"

combined = first + " " + second

print(combined)
print("Hi " * 3)

words = ["Python", "Deep", "Dive"]

result = " ".join(words)

print(result)

characters = []

for ch in "PYTHON":
    characters.append(ch.lower())

print("".join(characters))