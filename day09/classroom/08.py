'''
Example 08 — Return Values, Early Return and None
'''

def classify_number(number):
    if number < 0:
        return "Negative"

    if number == 0:
        return "Zero"

    return "Positive"


def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None


def display_message():
    print("Python Functions")


print(classify_number(-10))
print(classify_number(0))
print(classify_number(15))

print(find_first_even([1, 3, 7, 8, 9]))
print(find_first_even([1, 3, 5]))

result = display_message()
print("Returned:", result)