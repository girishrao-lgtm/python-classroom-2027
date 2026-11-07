text = input("Enter text: ")
pattern = input("Enter pattern: ")

if pattern == "":
    print("Pattern cannot be empty")
else:
    non_overlapping = text.count(pattern)

    overlapping = 0
    start = 0

    while True:
        position = text.find(pattern, start)

        if position == -1:
            break

        overlapping += 1
        start = position + 1

    print(f"Non-overlapping: {non_overlapping}")
    print(f"Overlapping: {overlapping}")