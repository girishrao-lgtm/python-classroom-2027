'''

Classroom 16 — Count words without split()
Concept: State transitions and word-boundary detection.
'''
text = input("Enter sentence: ")

word_count = 0
inside_word = False

for ch in text:

    if ch.isspace():
        inside_word = False

    elif not inside_word:
        word_count += 1
        inside_word = True

print(f"Number of words = {word_count}")