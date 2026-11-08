'''
Classroom 20 — Maximum Subarray Sum (Kadane's Algorithm)
'''
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = numbers[0]
max_sum = numbers[0]

start = 0
best_start = 0
best_end = 0

for i in range(1, len(numbers)):

    if numbers[i] > current_sum + numbers[i]:
        current_sum = numbers[i]
        start = i
    else:
        current_sum += numbers[i]

    if current_sum > max_sum:
        max_sum = current_sum
        best_start = start
        best_end = i

print(f"Maximum sum: {max_sum}")
print(f"Subarray: {numbers[best_start:best_end + 1]}")