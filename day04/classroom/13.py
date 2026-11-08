n = abs(int(input("Enter integer: ")))

count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10

print(f"Number of digits = {count}")