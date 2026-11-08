'''
Exercise 15 — Longest Consecutive Attendance Streak
'''
attendance = [1, 2, 3, 7, 8, 9, 10, 15, 16, 10]

days = set(attendance)

longest = 0
start_day = None

for day in days:
    if day - 1 not in days:
        current = day
        length = 0

        while current in days:
            current += 1
            length += 1

        if length > longest:
            longest = length
            start_day = day

print("Longest streak:", longest)

if start_day is not None:
    print("From:", start_day)
    print("To:", start_day + longest - 1)
    