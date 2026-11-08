'''
Exercise 19 — Three-Array Intersection
'''
a = [1, 2, 3, 4, 5, 5]
b = [2, 3, 5, 6, 7]
c = [0, 2, 5, 8, 9]

common = set(a) & set(b) & set(c)

print("Common distinct elements:", sorted(common))
print("Count:", len(common))