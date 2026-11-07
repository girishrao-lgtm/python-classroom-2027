units = int(input("Enter units consumed: "))

if units < 0:
    print("Invalid consumption")
else:
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = (
            100 * 3
            + 100 * 5
            + (units - 200) * 8
        )

    print(f"Bill = Rs. {bill:.2f}")