'''
Exercise 13 — Inventory Management with Constraints
'''

import sqlite3

connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
        CREATE TABLE inventory (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity >= 0)
        )
    """)

    connection.executemany(
        "INSERT INTO inventory VALUES (?, ?, ?)",
        [
            (101, "Laptop", 10),
            (102, "Mouse", 50)
        ]
    )

    connection.commit()

    def sell(product_id, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        with connection:
            cursor = connection.execute(
                """
                UPDATE inventory
                SET quantity = quantity - ?
                WHERE product_id = ?
                  AND quantity >= ?
                """,
                (quantity, product_id, quantity)
            )

            if cursor.rowcount != 1:
                raise ValueError(
                    "Product missing or insufficient stock"
                )

    sell(101, 3)

    try:
        sell(102, 100)
    except ValueError as error:
        print(error)

    print(connection.execute(
        "SELECT * FROM inventory"
    ).fetchall())

finally:
    connection.close()