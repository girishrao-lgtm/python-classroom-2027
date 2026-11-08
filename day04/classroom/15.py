n = int(input("Enter number: "))

if n < 2:
    print("Not prime")
else:
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            print("Not prime")
            break
    else:
        print("Prime")