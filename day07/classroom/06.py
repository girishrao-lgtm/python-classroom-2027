'''
Example 06 — Tuple Concatenation, Repetition and Comparison
'''
a = (10, 20)
b = (30, 40)

c = a + b
print(c)

print(a * 3)

print((10, 20) < (10, 30))
print((10, 50) > (10, 40))
print((10, 20) == (10, 20))
print((10, 20) < (10, 20, 30))

print(id(a))
a += (50,)
print(id(a))
print(a)
