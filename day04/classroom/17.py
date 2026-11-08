numbers = [10, 20, 10, 30, 20, 10, 40]

target = int(input("Enter target: "))

frequency = 0

for number in numbers:
    if number == target:
        frequency += 1

print(f"Frequency of {target} = {frequency}")