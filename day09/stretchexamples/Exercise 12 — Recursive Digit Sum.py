'''
Exercise 12 — Recursive Digit Sum
'''

def digit_sum(n):
    n = abs(n)

    if n < 10:
        return n

    return n % 10 + digit_sum(n // 10)


print(digit_sum(12345))
print(digit_sum(9876))
print(digit_sum(-456))
