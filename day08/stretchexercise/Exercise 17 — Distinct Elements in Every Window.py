'''
Exercise 17 — Distinct Elements in Every Window
'''
numbers = [1, 2, 1, 3, 4, 2, 3]
k = 4

frequency = {}
result = []

for right, x in enumerate(numbers):
    frequency[x] = frequency.get(x, 0) + 1

    if right >= k:
        outgoing = numbers[right - k]
        frequency[outgoing] -= 1

        if frequency[outgoing] == 0:
            del frequency[outgoing]

    if right >= k - 1:
        result.append(len(frequency))

print(result)