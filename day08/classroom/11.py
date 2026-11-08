'''
Example 11 — Dictionary Comprehensions
'''

squares = {x: x * x for x in range(1, 11)}
print(squares)

even_squares = {
    x: x * x
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_squares)

words = ["python", "java", "cpp"]

lengths = {word: len(word) for word in words}
print(lengths)

swapped = {value: key for key, value in squares.items()}
print(swapped)