'''
Stretch 16 — Prime-Based Security Gate
A security system accepts an integer only when it is prime and its digit sum is even.
'''
n = int(input("Enter security number: "))

is_prime = n >= 2

if is_prime:

    for divisor in range(2, int(n ** 0.5) + 1):

        if n % divisor == 0:
            is_prime = False
            break

temp = abs(n)
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

if is_prime and digit_sum % 2 == 0:
    print("ACCEPT")
else:
    print("REJECT")