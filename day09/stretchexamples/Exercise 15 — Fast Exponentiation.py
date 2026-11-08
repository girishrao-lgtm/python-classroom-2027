'''
Exercise 15 — Fast Exponentiation
'''

def power(base, exponent):
    if exponent == 0:
        return 1

    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("Zero cannot have a negative exponent")
        return 1 / power(base, -exponent)

    half = power(base, exponent // 2)

    if exponent % 2 == 0:
        return half * half

    return base * half * half


print(power(2, 10))
print(power(3, 5))
print(power(2, -3))
