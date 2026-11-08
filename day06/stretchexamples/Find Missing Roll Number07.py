'''
Stretch 07 — Find Missing Roll Number
'''
n = int(input("Total roll numbers: "))

roll_numbers = []

for i in range(n - 1):
    roll = int(input("Enter roll number: "))
    roll_numbers.append(roll)

expected_sum = n * (n + 1) // 2
actual_sum = sum(roll_numbers)

missing = expected_sum - actual_sum

print(f"Missing roll number: {missing}")