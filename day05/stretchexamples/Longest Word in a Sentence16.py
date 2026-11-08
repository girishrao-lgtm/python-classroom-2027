'''
Stretch 16 — Longest Word in a Sentence
Find the longest whitespace-separated word in a sentence. In case of ties, return the first one.
'''

sentence = input("Enter sentence: ")

words = sentence.split()

longest = ""

for word in words:

    if len(word) > len(longest):
        longest = word

if longest:
    print(f"Longest word = {longest}")
    print(f"Length = {len(longest)}")
else:
    print("No words found")