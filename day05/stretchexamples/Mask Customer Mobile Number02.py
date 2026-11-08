'''
Stretch 02 — Mask Customer Mobile Number
A customer service application must hide all but the last four digits of a ten-digit mobile number.
'''

mobile = input("Enter mobile number: ")

valid = len(mobile) == 10

for ch in mobile:
    if ch not in "0123456789":
        valid = False
        break

if valid:
    masked = "*" * 6 + mobile[-4:]
    print(f"Masked mobile = {masked}")
else:
    print("Invalid mobile number")