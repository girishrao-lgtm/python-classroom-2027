name = "Python"

before = id(name)

name = name + " Deep Dive"

after = id(name)

print(f"{name = }")
print(f"{before = }")
print(f"{after = }")