numbers = [12, 18, 25, 31, 42]

target = int(input("Enter target: "))

for index in range(len(numbers)):
    if numbers[index] == target:
        print(f"Found at index {index}")
        break
else:
    print("Element not found")