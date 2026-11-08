'''
Stretch 02 — Savings Goal Calculator
A student saves a fixed amount each week. Determine how many weeks are required to reach a target.

'''
weekly_saving = int(input("Weekly saving: "))
target = int(input("Target amount: "))

if target <= 0:
    print("Weeks required = 0")
elif weekly_saving <= 0:
    print("Target cannot be reached")
else:
    total = 0
    weeks = 0

    while total < target:
        total += weekly_saving
        weeks += 1

    print(f"Weeks required = {weeks}")
    print(f"Total saved = {total}")