'''
Delivery Charge Decision
Difficulty: Easy

An e-commerce platform charges ₹50 delivery for orders below ₹500, ₹25 for orders from ₹500 to below ₹1000, and zero for orders of ₹1000 or more. Premium members receive free delivery regardless of order amount.

Input: Order amount and premium status (yes or no) on separate lines.

Output: Delivery charge or INVALID for negative amount or unrecognized status.

'''
amount = float(input())
premium = input().strip().lower()

if amount < 0 or premium not in ("yes", "no"):
    print("INVALID")
elif premium == "yes":
    print(0)
elif amount < 500:
    print(50)
elif amount < 1000:
    print(25)
else:
    print(0)