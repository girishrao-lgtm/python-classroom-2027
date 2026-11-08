'''
Stretch 19 — Find Equilibrium Index
'''
numbers = [1, 3, 5, 2, 2]

total = sum(numbers)
left_sum = 0

found = False

for i in range(len(numbers)):

    right_sum = total - left_sum - numbers[i]

    if left_sum == right_sum:
        print(f"Equilibrium index: {i}")
        found = True
        break

    left_sum += numbers[i]

if not found:
    print("No equilibrium index")