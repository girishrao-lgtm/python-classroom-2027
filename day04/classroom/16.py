start = int(input("Enter start: "))
end = int(input("Enter end: "))

for number in range(max(2, start), end + 1):

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            break
    else:
        print(number)