'''
Exercise 16 — Recursive Binary Search
'''

def binary_search(numbers, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if numbers[mid] == target:
        return mid

    if numbers[mid] > target:
        return binary_search(numbers, target, left, mid - 1)

    return binary_search(numbers, target, mid + 1, right)


numbers = [5, 10, 15, 20, 25, 30, 35]

for target in [20, 5, 35, 100]:
    print(target, binary_search(numbers, target, 0, len(numbers) - 1))
    