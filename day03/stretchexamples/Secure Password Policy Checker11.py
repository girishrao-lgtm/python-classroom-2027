'''
Secure Password Policy Checker
Difficulty: Medium

A password is valid if it contains at least eight characters, includes at least one uppercase letter, one lowercase letter, one digit, and one character from @#$!, and contains no spaces.

Input: Password string.

Output: STRONG or WEAK.

'''
password = input()

has_upper = any(map(str.isupper, password))
has_lower = any(map(str.islower, password))
has_digit = any(map(str.isdigit, password))

has_special = (
    "@" in password
    or "#" in password
    or "$" in password
    or "!" in password
)

no_spaces = not any(map(str.isspace, password))

if (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_digit
    and has_special
    and no_spaces
):
    print("STRONG")
else:
    print("WEAK")