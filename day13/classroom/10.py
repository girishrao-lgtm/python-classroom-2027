'''
Example 10 — Assertions vs Runtime Validation
'''
def calculate_average(marks):
    if not marks:
        raise ValueError("Marks cannot be empty")

    assert all(
        isinstance(mark, (int, float))
        for mark in marks
    ), "Internal invariant violated"

    return sum(marks) / len(marks)


print(calculate_average([80, 90, 100]))

try:
    print(calculate_average([]))

except ValueError as error:
    print(error)