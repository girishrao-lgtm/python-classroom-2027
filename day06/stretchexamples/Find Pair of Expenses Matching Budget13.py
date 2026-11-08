'''
Stretch 13 — Find Pair of Expenses Matching Budget
'''
expenses = [1200, 800, 1500, 500, 2000]

budget = int(input("Enter target budget: "))

seen = set()
found = False

for expense in expenses:

    required = budget - expense

    if required in seen:
        print(f"Pair: {required}, {expense}")
        found = True
        break

    seen.add(expense)

if not found:
    print("No matching pair")