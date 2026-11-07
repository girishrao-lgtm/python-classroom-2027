a = 10
before = id(a)

a += 5

print(f"{a = }")
print(f"{before = }")
print(f"{id(a) = }")

numbers = [10, 20]
before_list = id(numbers)

numbers += [30]

print(f"{numbers = }")
print(f"{before_list == id(numbers) = }")