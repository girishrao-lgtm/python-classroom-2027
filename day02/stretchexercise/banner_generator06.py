text = input("Enter banner text: ")
separator = input("Enter separator: ")
count = int(input("Enter repetition count: "))

if count > 0:
    banner = separator.join([text] * count)
    print(banner)
else:
    print("Invalid repetition count")