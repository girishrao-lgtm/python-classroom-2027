target = int(input("Enter target: "))

for number in range(1, 101):
    if number == target:
        print(f"Found {target}")
        break
else:
    print("Target not found")