'''

Classroom 19 — Naive substring search
Concept: Sliding a pattern across a text and checking character matches.
'''

text = input("Enter text: ")
pattern = input("Enter pattern: ")

n = len(text)
m = len(pattern)

if m == 0:
    print("Empty pattern matches at index 0")

else:
    found = False

    for i in range(n - m + 1):

        match = True

        for j in range(m):

            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            print(f"Pattern found at index {i}")
            found = True

    if not found:
        print("Pattern not found")