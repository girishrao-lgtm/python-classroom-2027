'''
Exercise 04 — Tuple Rotation
'''
t = (10, 20, 30, 40, 50)
k = 2

n = len(t)

if n == 0:
    rotated = t
else:
    k %= n
    rotated = t[-k:] + t[:-k] if k else t

print("Original:", t)
print("Rotated:", rotated)