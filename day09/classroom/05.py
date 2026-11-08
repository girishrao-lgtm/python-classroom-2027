'''
Example 05 — Variable-Length Positional Arguments: *args
'''

def calculate_total(*numbers):
    print("Type:", type(numbers))
    print("Arguments:", numbers)
    return sum(numbers)


print(calculate_total())
print(calculate_total(10))
print(calculate_total(10, 20, 30))


def student_report(name, *marks):
    print("Name:", name)
    print("Marks:", marks)

    if marks:
        print("Average:", sum(marks) / len(marks))


student_report("Neha", 80, 90, 95)
