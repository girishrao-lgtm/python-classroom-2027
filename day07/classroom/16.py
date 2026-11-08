'''
Example 16 — Set Comprehensions
'''
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8]

squares = {x * x for x in numbers}
print(squares)

even_squares = {x * x for x in numbers if x % 2 == 0}
print(even_squares)

words = ["Python", "Java", "python", "JAVA", "C++"]

normalized = {word.lower() for word in words}
print(normalized)

lengths = {len(word) for word in words}
print(lengths)