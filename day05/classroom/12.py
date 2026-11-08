'''
Classroom 12 — Linear character search
Concept: First occurrence, last occurrence, and total matches.
'''
text = input("Enter text: ")
target = input("Enter one character: ")

if len(target) != 1:
    print("Target must be exactly one character")

else:
    first = -1
    last = -1
    count = 0

    for i in range(len(text)):

        if text[i] == target:

            if first == -1:
                first = i

            last = i
            count += 1

    print(f"First occurrence = {first}")
    print(f"Last occurrence = {last}")
    print(f"Frequency = {count}")

    print(f"Built-in find = {text.find(target)}")
    print(f"Built-in rfind = {text.rfind(target)}")