'''
Classroom 19 — Merge Two Sorted Lists
'''
a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

i = 0
j = 0

merged = []

while i < len(a) and j < len(b):

    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

while i < len(a):
    merged.append(a[i])
    i += 1

while j < len(b):
    merged.append(b[j])
    j += 1

print(f"Merged: {merged}")