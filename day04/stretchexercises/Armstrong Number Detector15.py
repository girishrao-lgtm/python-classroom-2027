'''
Stretch 15 — Armstrong Number Detector
Determine whether a non-negative integer is an Armstrong number.
'''
n = int(input("Enter number: "))

if n < 0:
    print("Not an Armstrong number")
else:
    digits = len(str(n))

    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
        