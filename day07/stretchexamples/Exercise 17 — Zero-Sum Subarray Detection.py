'''
Exercise 17 — Zero-Sum Subarray Detection
'''
numbers = [4, 2, -3, 1, 6]

prefix_sum = 0
seen = {0}
found = False

for x in numbers:
    prefix_sum += x

    if prefix_sum in seen:
        found = True
        break

    seen.add(prefix_sum)

print("Zero-sum subarray exists:", found)
