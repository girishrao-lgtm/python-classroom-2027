'''
Classroom 18 — Run-length encoding
Concept: Consecutive-character grouping.

Example: aaabbcccc becomes a3b2c4.
'''
text = input("Enter string: ")

if not text:
    print("Encoded string = ")

else:
    result = []
    count = 1

    for i in range(1, len(text)):

        if text[i] == text[i - 1]:
            count += 1

        else:
            result.append(text[i - 1])
            result.append(str(count))
            count = 1

    result.append(text[-1])
    result.append(str(count))

    print(f"Encoded string = {''.join(result)}")