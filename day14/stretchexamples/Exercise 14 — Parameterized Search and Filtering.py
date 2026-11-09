'''
Exercise 14 — Parameterized Search and Filtering
'''

import sqlite3

connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price INTEGER
        )
    """)

    connection.executemany(
        "INSERT INTO products VALUES (?, ?, ?, ?)",
        [
            (1, "Laptop", "Electronics", 50000),
            (2, "Mouse", "Electronics", 500),
            (3, "Desk", "Furniture", 5000),
            (4, "Chair", "Furniture", 3000)
        ]
    )

    connection.commit()

    def search(category, minimum, maximum):
        return connection.execute(
            """
            SELECT name, price
            FROM products
            WHERE category = ?
              AND price BETWEEN ? AND ?
            ORDER BY price
            """,
            (category, minimum, maximum)
        ).fetchall()

    print(search("Electronics", 100, 60000))
    print(search("Furniture", 1000, 4000))

finally:
    connection.close()