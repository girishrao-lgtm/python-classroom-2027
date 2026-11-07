'''
Electricity Bill with Surcharge
Difficulty: Medium

Calculate an electricity bill using progressive slabs: first 100 units at ₹3, next 100 at ₹5, and remaining units at ₹8. Add a 10% surcharge if the calculated bill exceeds ₹1,000.

Input: Nonnegative integer units.

Output: Final bill with two decimal places, or INVALID.

'''
units = int(input())

if units < 0:
    print("INVALID")
else:
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 8

    if bill > 1000:
        bill *= 1.10

    print(f"{bill:.2f}")