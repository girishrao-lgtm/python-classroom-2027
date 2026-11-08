'''
Stretch 12 — Find All Positions of a Keyword
A log-processing system must report every starting position of a keyword within a message.
'''

message = input("Enter message: ")
keyword = input("Enter keyword: ")

positions = []

if keyword == "":
    print("Keyword cannot be empty")

else:
    start = 0

    while True:

        index = message.find(keyword, start)

        if index == -1:
            break

        positions.append(index)
        start = index + 1

    print(f"Positions = {positions}")
    print(f"Total matches = {len(positions)}")