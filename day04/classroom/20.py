numbers = [45, 12, 78, 78, 34, 56, 90, 90]

largest = None
second_largest = None

for number in numbers:

    if largest is None or number > largest:
        second_largest = largest
        largest = number

    elif number != largest:
        if second_largest is None or number > second_largest:
            second_largest = number

if second_largest is None:
    print("No second-largest distinct number")
else:
    print(f"Largest = {largest}")
    print(f"Second largest = {second_largest}")