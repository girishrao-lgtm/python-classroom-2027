number = int(input("Enter number: "))

result = (
    "Positive" if number > 0
    else "Negative" if number < 0
    else "Zero"
)

print(result)