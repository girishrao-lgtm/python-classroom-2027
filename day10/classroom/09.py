'''
Example 09 — Generator Expressions vs List Comprehensions
'''
numbers = [1, 2, 3, 4, 5]

squares_list = [x * x for x in numbers]
squares_generator = (x * x for x in numbers)

print(type(squares_list))
print(type(squares_generator))

print(squares_list)

print(next(squares_generator))
print(next(squares_generator))

print(list(squares_generator))
print(list(squares_generator))