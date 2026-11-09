'''

Exercise 12 — Bank Transfer with Transaction Rollback
'''
import sqlite3

connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
        CREATE TABLE accounts (
            id TEXT PRIMARY KEY,
            balance INTEGER NOT NULL CHECK(balance >= 0)
        )
    """)

    connection.executemany(
        "INSERT INTO accounts VALUES (?, ?)",
        [
            ("A101", 5000),
            ("A102", 2000)
        ]
    )

    connection.commit()

    def transfer(source, destination, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")

        with connection:
            cursor = connection.execute(
                """
                UPDATE accounts
                SET balance = balance - ?
                WHERE id = ? AND balance >= ?
                """,
                (amount, source, amount)
            )

            if cursor.rowcount != 1:
                raise ValueError("Insufficient funds")

            cursor = connection.execute(
                """
                UPDATE accounts
                SET balance = balance + ?
                WHERE id = ?
                """,
                (amount, destination)
            )

            if cursor.rowcount != 1:
                raise ValueError("Destination missing")

    transfer("A101", "A102", 1000)

    try:
        transfer("A101", "A102", 10000)
    except ValueError as error:
        print(error)

    print(connection.execute(
        "SELECT * FROM accounts"
    ).fetchall())

finally:
    connection.close()