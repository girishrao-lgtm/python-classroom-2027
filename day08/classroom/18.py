'''
Example 18 — Two Sum Using a Hash Map
'''

numbers = [2, 7, 11, 15]
target = 9

seen = {}
answer = None

for i, x in enumerate(numbers):
    complement = target - x

    if complement in seen:
        answer = (seen[complement], i)
        break

    seen[x] = i

print("Indices:", answer)