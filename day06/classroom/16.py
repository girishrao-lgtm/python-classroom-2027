'''
Classroom 16 — Reverse a List In Place
'''
numbers = [10, 20, 30, 40, 50, 60]

left = 0
right = len(numbers) - 1

while left < right:

    numbers[left], numbers[right] = numbers[right], numbers[left]

    left += 1
    right -= 1

print(f"Reversed: {numbers}")