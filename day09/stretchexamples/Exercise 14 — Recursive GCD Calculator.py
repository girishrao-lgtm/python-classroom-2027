'''
Exercise 14 — Recursive GCD Calculator
'''

def gcd(a, b):
    if b == 0:
        return abs(a)

    return gcd(b, a % b)


print(gcd(48, 18))
print(gcd(100, 25))
print(gcd(17, 13))
