'''
Example 10 — Lazy Evaluation and Execution Timing
'''

def square(number):
    print("Processing:", number)
    return number * number


numbers = [1, 2, 3, 4]

print("Creating list")

result_list = [square(x) for x in numbers]

print("List created")

print("Creating generator")

result_generator = (square(x) for x in numbers)

print("Generator created")

print(next(result_generator))
print(next(result_generator))

print("Remaining:", list(result_generator))