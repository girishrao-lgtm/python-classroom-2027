'''
Classroom 05 — References and Aliasing
'''
a = [10, 20, 30]
b = a

print(f"a: {a}")
print(f"b: {b}")

print(f"a id: {id(a)}")
print(f"b id: {id(b)}")

print(f"a is b: {a is b}")

b[0] = 999

print(f"a after modification: {a}")
print(f"b after modification: {b}")