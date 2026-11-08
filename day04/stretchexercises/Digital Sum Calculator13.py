'''
Stretch 13 — Digital Sum Calculator
Calculate the sum of digits of a given integer without converting it to a string.
'''
n = abs(int(input("Enter integer: ")))

digit_sum = 0

while n > 0:

    digit = n % 10
    digit_sum += digit
    n //= 10

print(f"Digit sum = {digit_sum}")