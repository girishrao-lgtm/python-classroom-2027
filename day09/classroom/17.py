'''
Example 17 — Recursive Functions and Call Stack
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)


def print_reverse(n):
    if n == 0:
        return

    print(n)
    print_reverse(n - 1)


print("Factorial:", factorial(5))
print("Sum:", sum_n(5))

print_reverse(5)