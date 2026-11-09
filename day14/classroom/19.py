'''
Example 19 — Parameterized SQL and Transactions
'''

import sqlite3

connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
        CREATE TABLE accounts (
            account_id TEXT PRIMARY KEY,
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

    try:
        with connection:
            amount = 1000

            cursor = connection.execute(
                """
                UPDATE accounts
                SET balance = balance - ?
                WHERE account_id = ?
                  AND balance >= ?
                """,
                (amount, "A101", amount)
            )

            if cursor.rowcount != 1:
                raise ValueError("Insufficient funds")

            connection.execute(
                """
                UPDATE accounts
                SET balance = balance + ?
                WHERE account_id = ?
                """,
                (amount, "A102")
            )

    except (sqlite3.Error, ValueError) as error:
        print("Transaction failed:", error)

    for row in connection.execute(
        "SELECT * FROM accounts"
    ):
        print(row)

finally:
    connection.close()