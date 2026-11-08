'''
Example 19 — Prefix Sum and Subarray Sum Equals K
'''

numbers = [1, 2, 3, -2, 2, 1]
k = 3

prefix = 0
frequency = {0: 1}
count = 0

for x in numbers:
    prefix += x

    count += frequency.get(prefix - k, 0)

    frequency[prefix] = frequency.get(prefix, 0) + 1

print("Subarrays with sum K:", count)