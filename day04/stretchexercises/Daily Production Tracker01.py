'''
Stretch 01 — Daily Production Tracker
A factory produces a fixed number of units daily. 
Calculate the total production over N days, 
assuming production increases by 5 units each day.
'''
days = int(input("Enter number of days: "))
production = int(input("Enter day 1 production: "))

total = 0

for day in range(1, days + 1):
    print(f"Day {day}: {production} units")
    total += production
    production += 5

print(f"Total production = {total}")