age = int(input("Enter age (1-120): "))

while age < 1 or age > 120:
    print("Invalid age")
    age = int(input("Enter age again: "))

print(f"Accepted age: {age}")