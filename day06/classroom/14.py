'''
Classroom 14 — Frequency Counting Without Dictionary
'''

numbers = [10, 20, 10, 30, 20, 10, 40]

for i in range(len(numbers)):

    already_counted = False

    for j in range(i):
        if numbers[i] == numbers[j]:
            already_counted = True
            break

    if already_counted:
        continue

    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    print(f"{numbers[i]}: {count}")