'''
Stretch 13 — Vehicle Registration Palindrome Check
A vehicle monitoring system extracts the numeric portion of a registration code and checks whether it forms a palindrome.

Example: KA03AB1221 has numeric suffix 1221.
'''
registration = input("Enter registration code: ")

digits = ""

for ch in registration:
    if "0" <= ch <= "9":
        digits += ch

if digits == "":
    print("No digits found")

elif digits == digits[::-1]:
    print("Numeric sequence is palindrome")

else:
    print("Numeric sequence is not palindrome")