'''
Stretch 18 — Warehouse Storage Grid
A warehouse has R rows and C columns. Generate a unique storage location code for every cell.

'''
rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

for row in range(1, rows + 1):

    for column in range(1, columns + 1):

        print(f"R{row}C{column}", end=" ")

    print()