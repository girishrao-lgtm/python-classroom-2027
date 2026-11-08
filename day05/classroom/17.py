'''
Classroom 17 — Anagram checking using frequency counts
Concept: Character frequency comparison.
'''
first = input("Enter first string: ")
second = input("Enter second string: ")

if len(first) != len(second):
    print("Not anagrams")

else:
    frequency = {}

    for ch in first:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in second:
        frequency[ch] = frequency.get(ch, 0) - 1

    is_anagram = True

    for count in frequency.values():
        if count != 0:
            is_anagram = False
            break

    print("Anagrams" if is_anagram else "Not anagrams")