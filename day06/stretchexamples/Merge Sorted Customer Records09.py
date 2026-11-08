'''
Stretch 09 — Merge Sorted Customer Records
'''
a = [101, 105, 109, 115]
b = [102, 106, 110, 120]

merged = []

i = 0
j = 0

while i < len(a) and j < len(b):

    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

merged.extend(a[i:])
merged.extend(b[j:])

print(f"Merged records: {merged}")