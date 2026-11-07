a = [10, 20, 30]
b = a

print(f"{id(a) = }")
print(f"{id(b) = }")
print(f"{a is b = }")

b.append(40)

print(f"{a = }")
print(f"{b = }")