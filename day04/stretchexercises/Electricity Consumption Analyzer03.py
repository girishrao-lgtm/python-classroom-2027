'''
Stretch 03 — Electricity Consumption Analyzer
Read electricity consumption for N days and calculate the total, average, and number of days exceeding 100 units.
'''
n = int(input("Number of days: "))

total = 0
high_usage_days = 0

for day in range(1, n + 1):
    units = int(input(f"Day {day} units: "))

    total += units

    if units > 100:
        high_usage_days += 1

print(f"Total consumption = {total}")

if n > 0:
    print(f"Average consumption = {total / n:.2f}")

print(f"High usage days = {high_usage_days}")