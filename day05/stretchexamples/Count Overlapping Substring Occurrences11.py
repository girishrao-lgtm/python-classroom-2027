'''
Stretch 11 — Count Overlapping Substring Occurrences
Given a text and a pattern, count all occurrences, including overlapping matches.

Example: aaaaa with pattern aaa gives 3.

'''
text = input("Enter text: ")
pattern = input("Enter pattern: ")

n = len(text)
m = len(pattern)

count = 0

if m == 0:
    print("Pattern must not be empty")

else:
    for i in range(n - m + 1):

        matched = True

        for j in range(m):
            if text[i + j] != pattern[j]:
                matched = False
                break

        if matched:
            count += 1

    print(f"Occurrences = {count}")