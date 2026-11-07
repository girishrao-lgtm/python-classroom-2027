'''
Online Shopping Discount Engine
Difficulty: Medium

An online store offers a 5% discount for purchases of ₹1,000–₹4,999, 10% for ₹5,000–₹9,999, and 15% for ₹10,000 or more. Premium members receive an additional 5 percentage points of discount.

Input: Integer purchase amount and premium status (yes or no) on separate lines.

Output: Final amount with two decimal places, or INVALID.

'''
amount = int(input())
premium = input().strip().lower()

if amount < 0 or premium not in ("yes", "no"):
    print("INVALID")
else:
    if amount >= 10000:
        discount = 15
    elif amount >= 5000:
        discount = 10
    elif amount >= 1000:
        discount = 5
    else:
        discount = 0

    if premium == "yes":
        discount += 5

    final_amount = amount * (100 - discount) / 100

    print(f"{final_amount:.2f}")