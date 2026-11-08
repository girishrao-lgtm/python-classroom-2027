'''
Stretch 14 — Palindrome Number Validator
Determine whether an integer reads the same forward and backward.
'''
n = int(input("Enter integer: "))

original = n
reverse = 0

if n < 0:
    print("Not palindrome")
else:

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    if original == reverse:
        print("Palindrome")
    else:
        print("Not palindrome")

        