'''
Date Validity Checker
Difficulty: Medium+

Given a day, month, and year, determine whether the date is valid in the Gregorian calendar.

Handle 30-day months, 31-day months, February, and leap years. Accept years from 1 through 9999.

Input: Day, month, year on separate lines.

Output: VALID or INVALID.

'''
day = int(input())
month = int(input())
year = int(input())

if not (1 <= year <= 9999 and 1 <= month <= 12):
    print("INVALID")
else:
    leap = (
        year % 400 == 0
        or (year % 4 == 0 and year % 100 != 0)
    )

    if month == 2:
        max_days = 29 if leap else 28
    elif month in (4, 6, 9, 11):
        max_days = 30
    else:
        max_days = 31

    if 1 <= day <= max_days:
        print("VALID")
    else:
        print("INVALID")