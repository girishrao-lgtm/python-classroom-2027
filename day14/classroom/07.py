'''
Example 07 — Processing Large Files Lazily
'''

from pathlib import Path

path = Path("large_numbers.txt")

with path.open("w", encoding="utf-8") as file:
    for number in range(1, 100001):
        file.write(f"{number}\n")

total = 0
count = 0

with path.open("r", encoding="utf-8") as file:
    for line in file:
        number = int(line.strip())

        total += number
        count += 1

print("Count:", count)
print("Sum:", total)
print("Average:", total / count)