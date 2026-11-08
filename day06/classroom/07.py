'''

Classroom 07 — Shallow Copy vs Deep Copy
'''
import copy

original = [[10, 20], [30, 40]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 999

print(f"Original: {original}")
print(f"Shallow: {shallow}")
print(f"Deep: {deep}")

print(original[0] is shallow[0])
print(original[0] is deep[0])
