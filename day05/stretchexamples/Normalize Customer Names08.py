'''
Stretch 08 — Normalize Customer Names
A customer database contains names with inconsistent spacing and capitalization. Remove extra whitespace and convert the name to title case.
'''

name = input("Enter customer name: ")

words = name.split()

normalized_words = []

for word in words:
    normalized_words.append(word.title())

normalized_name = " ".join(normalized_words)

print(f"Normalized name = {normalized_name}")