'''
Exercise 03 — Coordinate Movement Tracker
'''
position = (0, 0)

commands = [
    ("UP", 5),
    ("RIGHT", 3),
    ("DOWN", 2),
    ("LEFT", 1)
]

x, y = position

for direction, steps in commands:
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "RIGHT":
        x += steps
    elif direction == "LEFT":
        x -= steps

position = (x, y)

print("Final position:", position)
print("Manhattan distance:", abs(x) + abs(y))