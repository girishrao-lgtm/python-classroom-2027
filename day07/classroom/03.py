'''
Example 03 — Tuple Packing and Unpacking
'''
student = "Amit", 21, 85

name, age, marks = student
print(name, age, marks)

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers
print(first)
print(middle)
print(last)

a, b = 10, 20
a, b = b, a

print(a, b)