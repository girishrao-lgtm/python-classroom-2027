total = 0
count = 0

while True:
    number = int(input("Enter number (-1 to stop): "))

    if number == -1:
        break

    total += number
    count += 1

if count > 0:
    print(f"Sum = {total}")
    print(f"Average = {total / count:.2f}")
else:
    print("No numbers entered")