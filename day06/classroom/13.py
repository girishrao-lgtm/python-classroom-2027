'''
Classroom 13 — Linear Search
'''
numbers = [12, 45, 78, 23, 56, 90]

target = int(input("Enter target: "))

position = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        position = i
        break

if position == -1:
    print("Not found")
else:
    print(f"Found at index {position}")