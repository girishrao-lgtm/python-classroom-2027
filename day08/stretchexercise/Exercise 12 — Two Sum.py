'''
Exercise 12 — Two Sum
'''

numbers = [3, 2, 4]
target = 6

seen = {}
answer = (-1, -1)

for i, x in enumerate(numbers):
    complement = target - x

    if complement in seen:
        answer = (seen[complement], i)
        break

    seen[x] = i

print(answer)

