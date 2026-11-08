'''
Example 14 — Lambda Expressions
'''

square = lambda x: x * x

print(square(5))

add = lambda a, b: a + b

print(add(10, 20))

students = [
    ("Amit", 85),
    ("Neha", 95),
    ("Ravi", 75)
]

print(sorted(students, key=lambda student: student[1]))

print(sorted(students, key=lambda student: -student[1]))

numbers = [10, 5, 20, 15]

print(sorted(numbers, key=lambda x: abs(x - 12)))