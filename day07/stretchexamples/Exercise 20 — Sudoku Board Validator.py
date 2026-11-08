'''
Exercise 20 — Sudoku Board Validator
'''

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

seen = set()
valid = True

for row in range(9):
    for col in range(9):
        value = board[row][col]

        if value == ".":
            continue

        if value not in "123456789":
            valid = False
            break

        row_key = ("row", row, value)
        col_key = ("col", col, value)
        box_key = ("box", row // 3, col // 3, value)

        if (
            row_key in seen
            or col_key in seen
            or box_key in seen
        ):
            valid = False
            break

        seen.add(row_key)
        seen.add(col_key)
        seen.add(box_key)

    if not valid:
        break

print("Valid Sudoku:", valid)
