'''
Stretch 05 — Password Strength Validator
A password is accepted if it contains at least eight characters, one uppercase ASCII letter, one lowercase ASCII letter, one digit, and one special character.
'''

password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:

    if "A" <= ch <= "Z":
        has_upper = True

    elif "a" <= ch <= "z":
        has_lower = True

    elif "0" <= ch <= "9":
        has_digit = True

    else:
        has_special = True

valid = (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_digit
    and has_special
)

print("STRONG" if valid else "WEAK")