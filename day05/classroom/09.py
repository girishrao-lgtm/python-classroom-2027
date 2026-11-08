'''
Classroom 09 — Count vowels, consonants, digits, and spaces
Concept: Character classification through iteration.
'''
text = input("Enter text: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
others = 0

for ch in text:

    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

    elif ch.isdigit():
        digits += 1

    elif ch.isspace():
        spaces += 1

    else:
        others += 1

print(f"Vowels = {vowels}")
print(f"Consonants = {consonants}")
print(f"Digits = {digits}")
print(f"Whitespace characters = {spaces}")
print(f"Others = {others}")