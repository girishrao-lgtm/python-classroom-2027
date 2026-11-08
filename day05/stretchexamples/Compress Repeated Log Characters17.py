'''
Stretch 17 — Compress Repeated Log Characters
A logging system wants to compress consecutive repeated characters using run-length encoding.

Example: AAAABCCDDDD becomes A4B1C2D4.
'''

text = input("Enter log string: ")

result = []

i = 0

while i < len(text):

    current = text[i]
    count = 0

    while i < len(text) and text[i] == current:
        count += 1
        i += 1

    result.append(current)
    result.append(str(count))

compressed = "".join(result)

print(f"Compressed = {compressed}")
print(f"Original length = {len(text)}")
print(f"Compressed length = {len(compressed)}")

