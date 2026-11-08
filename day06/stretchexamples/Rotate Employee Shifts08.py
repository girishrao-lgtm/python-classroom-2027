'''
Stretch 08 — Rotate Employee Shifts
'''
employees = ["A", "B", "C", "D", "E"]

k = int(input("Shift rotation count: "))

n = len(employees)

if n > 0:
    k %= n

    if k != 0:
        employees = employees[-k:] + employees[:-k]

print(f"Updated shifts: {employees}")
