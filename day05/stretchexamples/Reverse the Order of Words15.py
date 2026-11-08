'''
Stretch 15 — Reverse the Order of Words
Reverse the order of words in a sentence without reversing the characters inside individual words.
'''

sentence = input("Enter sentence: ")

words = sentence.split()

result = []

for i in range(len(words) - 1, -1, -1):
    result.append(words[i])

reversed_sentence = " ".join(result)

print(f"Result = {reversed_sentence}")