'''
Stretch 14 — Longest Increasing Sales Streak
'''
sales = [100, 120, 150, 90, 110, 140, 160, 80]

if not sales:
    print("No sales data")
else:
    current = 1
    longest = 1

    start = 0
    best_start = 0

    for i in range(1, len(sales)):

        if sales[i] > sales[i - 1]:
            current += 1
        else:
            current = 1
            start = i

        if current > longest:
            longest = current
            best_start = start

    print(f"Longest streak: {longest}")
    print(f"Values: {sales[best_start:best_start + longest]}")