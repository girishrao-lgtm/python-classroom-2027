'''
Stretch 04 — Employee Attendance Counter
A company records employee attendance as P or A. Count present and absent days.
'''
days = int(input("Enter working days: "))

present = 0
absent = 0

for day in range(1, days + 1):

    while True:
        status = input(f"Day {day} (P/A): ").upper()

        if status == "P" or status == "A":
            break

        print("Invalid attendance status")

    if status == "P":
        present += 1
    else:
        absent += 1

print(f"Present = {present}")
print(f"Absent = {absent}")

if days > 0:
    print(f"Attendance percentage = {present / days * 100:.2f}%")