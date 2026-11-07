numbers = [10, 20, 30]

before = id(numbers)

numbers[0] = 99
numbers.append(40)

after = id(numbers)

print(f"{numbers = }")
print(f"{before = }")
print(f"{after = }")
print(f"{before == after = }")