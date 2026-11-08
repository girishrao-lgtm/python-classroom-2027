'''
Stretch 03 — Extract Information from a Product Code
A product code follows the format CAT-2026-0045. Extract its category, year, and serial number.
'''
code = input("Enter product code: ")

valid = (
    len(code) == 13
    and code[3] == "-"
    and code[8] == "-"
    and code[:3].isalpha()
    and code[4:8].isascii()
    and code[4:8].isdigit()
    and code[9:].isascii()
    and code[9:].isdigit()
)

if valid:
    category = code[:3]
    year = code[4:8]
    serial = code[9:]

    print(f"Category = {category}")
    print(f"Year = {year}")
    print(f"Serial = {serial}")
else:
    print("Invalid product code")