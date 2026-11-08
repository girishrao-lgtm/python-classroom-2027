'''
Classroom 11 — Character frequency without a dictionary
Concept: Nested-loop frequency counting.
'''
text = input("Enter text: ")

for i in range(len(text)):

    already_counted = False

    for j in range(i):
        if text[i] == text[j]:
            already_counted = True
            break

    if already_counted:
        continue

    count = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            count += 1

    print(f"{text[i]!r}: {count}")

    