'''
Employee Performance Bonus
Difficulty: Medium

An employee receives a bonus based on rating: rating 5 earns 20%, rating 4 earns 15%, rating 3 earns 10%, and ratings 1–2 earn zero. Employees with at least five completed years of service receive an additional 5 percentage points.

Input: Monthly salary, rating, and completed years of service on separate lines.

Output: Bonus amount with two decimal places, or INVALID for nonpositive salary, rating outside 1–5, or negative service years.
'''
salary = float(input())
rating = int(input())
years = int(input())

if salary <= 0 or not (1 <= rating <= 5) or years < 0:
    print("INVALID")
else:
    if rating == 5:
        bonus_percentage = 20
    elif rating == 4:
        bonus_percentage = 15
    elif rating == 3:
        bonus_percentage = 10
    else:
        bonus_percentage = 0

    if years >= 5:
        bonus_percentage += 5

    bonus = salary * bonus_percentage / 100

    print(f"{bonus:.2f}")