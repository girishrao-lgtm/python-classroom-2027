'''
Stretch 02 — Daily Sales Tracker
'''
n = int(input("Number of days: "))

sales = []

for day in range(1, n + 1):
    amount = float(input(f"Day {day} sales: "))
    sales.append(amount)

if not sales:
    print("No sales data")
else:
    total = sum(sales)
    average = total / n

    above_average = 0

    for amount in sales:
        if amount > average:
            above_average += 1

    print(f"Total sales: {total:.2f}")
    print(f"Average sales: {average:.2f}")
    print(f"Days above average: {above_average}")