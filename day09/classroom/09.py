'''
Example 09 — Multiple Return Values and Tuple Unpacking
'''

def analyze_numbers(numbers):
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / len(numbers)

    return total, minimum, maximum, average


result = analyze_numbers([10, 20, 30, 40, 50])

print(result)
print(type(result))

total, minimum, maximum, average = result

print("Total:", total)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)