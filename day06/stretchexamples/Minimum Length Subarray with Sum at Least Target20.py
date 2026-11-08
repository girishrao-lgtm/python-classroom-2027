'''
Stretch 20 — Minimum Length Subarray with Sum at Least Target
'''

numbers = [2, 3, 1, 2, 4, 3]

target = int(input("Enter target: "))

left = 0
current_sum = 0

min_length = float("inf")
best_start = -1
best_end = -1

for right in range(len(numbers)):

    current_sum += numbers[right]

    while current_sum >= target and left <= right:

        length = right - left + 1

        if length < min_length:
            min_length = length
            best_start = left
            best_end = right

        current_sum -= numbers[left]
        left += 1

if min_length == float("inf"):
    print("No valid subarray")
else:
    print(f"Minimum length: {min_length}")
    print(f"Subarray: {numbers[best_start:best_end + 1]}")