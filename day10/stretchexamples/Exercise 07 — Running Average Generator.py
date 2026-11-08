'''
Exercise 07 — Running Average Generator
'''

def running_average(numbers):
    total = 0
    for count, number in enumerate(numbers, start=1):
        total += number

        yield total / count


numbers = [10, 20, 30, 40, 50]

for average in running_average(numbers):
    print(f"{average:.2f}")