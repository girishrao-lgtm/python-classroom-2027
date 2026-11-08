'''
Classroom 02 — Positive and negative indexing
Concept: Accessing individual characters using integer indices.
'''
text = "PYTHON"

print(f"First character = {text[0]}")
print(f"Second character = {text[1]}")
print(f"Last character = {text[-1]}")
print(f"Second last = {text[-2]}")

for i in range(len(text)):
    print(f"Index {i}: {text[i]}")

print("Negative indexing:")

for i in range(-len(text), 0):
    print(f"Index {i}: {text[i]}")