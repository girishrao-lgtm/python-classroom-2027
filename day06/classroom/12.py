'''
Classroom 12 — Sum, Average, Minimum, and Maximum
'''

numbers = [45, 12, 78, 34, 90, 23]

total = 0
minimum = numbers[0]
maximum = numbers[0]

for number in numbers:
    total += number

    minimum = min(minimum, number)

    maximum = max(maximum, number)

average = total / len(numbers)

print(f"Sum: {total}")
print(f"Average: {average:.2f}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")