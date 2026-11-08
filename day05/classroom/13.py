'''
Classroom 13 — Reverse a string without slicing
Concept: Two-pointer-style reverse traversal.
'''
text = input("Enter text: ")

result = []

for i in range(len(text) - 1, -1, -1):
    result.append(text[i])

reversed_text = "".join(result)

print(f"Original = {text}")
print(f"Reversed = {reversed_text}")