'''
Example 09 — Dictionary References, Aliasing and Shallow Copy
'''
original = {
    "name": "Amit",
    "marks": [80, 90]
}

alias = original
shallow = original.copy()

print(id(original))
print(id(alias))
print(id(shallow))

alias["name"] = "Ravi"
shallow["marks"].append(100)

print(original)
print(alias)
print(shallow)

shallow["name"] = "Neha"

print(original)
print(shallow)