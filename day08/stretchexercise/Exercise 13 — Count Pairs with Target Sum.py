'''
Exercise 13 — Count Pairs with Target Sum
'''

numbers = [1, 5, 7, -1, 5]
target = 6

frequency = {}
count = 0

for x in numbers:
    complement = target - x

    count += frequency.get(complement, 0)

    frequency[x] = frequency.get(x, 0) + 1

print("Number of index pairs:", count)