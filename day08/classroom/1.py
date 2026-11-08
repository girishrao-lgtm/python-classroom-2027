'''
Example 01 — Dictionary Creation and Initialization
'''
a = {}
b = {"name": "Amit", "age": 21, "marks": 85}
c = {"name": "Neha", "age": 22}
d = {"a": 10, "b": 20}
e = dict.fromkeys(["Math", "Python", "Java"], 0)

print(a, type(a))
print(b)
print(c)
print(d)
print(e)

print(len(b))