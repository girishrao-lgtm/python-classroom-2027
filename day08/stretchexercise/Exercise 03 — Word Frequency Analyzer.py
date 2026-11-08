'''
Exercise 03 — Word Frequency Analyzer
'''

import string

text = "Python is powerful. Python is simple, and Python is popular."

frequency = {}

for word in text.lower().split():
    word = word.strip(string.punctuation)

    if word:
        frequency[word] = frequency.get(word, 0) + 1

for word, count in sorted(frequency.items()):
    print(word, count)