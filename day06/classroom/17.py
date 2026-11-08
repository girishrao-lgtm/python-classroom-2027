'''

Classroom 17 — Second-Largest Distinct Element
'''

numbers = [45, 90, 12, 90, 78, 34, 78]

largest = None
second = None

for number in numbers:

    if largest is None or number > largest:
        second = largest
        largest = number

    elif number != largest and (second is None or number > second):
        second = number

if second is None:
    print("No second-largest distinct element")
else:
    print(f"Largest: {largest}")
    print(f"Second largest: {second}")