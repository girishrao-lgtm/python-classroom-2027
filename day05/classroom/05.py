'''
Classroom 05 — String immutability
Concept: Strings cannot be modified in place.
'''

text = "Python"

print(f"Original = {text}")

try:
    text[0] = "J"
except TypeError as error:
    print(f"Error: {error}")

modified = "J" + text[1:]

print(f"Original remains = {text}")
print(f"New string = {modified}")