'''
Example 19 — Recursive Binary Search
'''

def binary_search(numbers, target, left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if numbers[mid] == target:
        return mid

    if numbers[mid] > target:
        return binary_search(numbers, target, left, mid - 1)

    return binary_search(numbers, target, mid + 1, right)


numbers = [10, 20, 30, 40, 50, 60, 70]

target = 50

index = binary_search(numbers, target, 0, len(numbers) - 1)

print("Index:", index)