'''
Exercise 18 — Unique Grid Coordinates
'''

commands = "UURDDLULRR"

x = 0
y = 0

visited = {(0, 0)}

for command in commands:
    if command == "U":
        y += 1
    elif command == "D":
        y -= 1
    elif command == "L":
        x -= 1
    elif command == "R":
        x += 1

    visited.add((x, y))

print("Final position:", (x, y))
print("Unique visited positions:", len(visited))
print("Visited coordinates:", sorted(visited))
