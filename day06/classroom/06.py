'''
Classroom 06 — Shallow Copying
'''
original = [10, 20, 30]

copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

copy1[0] = 100
copy2[1] = 200
copy3[2] = 300

print(f"Original: {original}")
print(f"Copy1: {copy1}")
print(f"Copy2: {copy2}")
print(f"Copy3: {copy3}")

print(original is copy1)
print(original == [10, 20, 30])
