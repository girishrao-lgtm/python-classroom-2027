'''
Stretch 01 — Employee ID Format Validator
An organization assigns employee IDs in the format EMP-1234. Validate that the ID begins with EMP-, has exactly eight characters, and ends with four ASCII digits.
'''

employee_id = input("Enter employee ID: ")

valid = True

if len(employee_id) != 8 or employee_id[:4] != "EMP-":
    valid = False

else:
    for ch in employee_id[4:]:
        if ch not in "0123456789":
            valid = False
            break

print("VALID" if valid else "INVALID")