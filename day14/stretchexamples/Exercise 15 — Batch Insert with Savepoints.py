'''
Exercise 15 — Batch Insert with Savepoints
'''

import sqlite3

connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            marks INTEGER CHECK(marks BETWEEN 0 AND 100)
        )
    """)

    connection.commit()

    records = [
        (101, "Alice", 90),
        (102, "Bob", 120),
        (103, "Charlie", 85)
    ]

    connection.execute("BEGIN")

    try:
        for record in records:
            connection.execute("SAVEPOINT one_record")

            try:
                connection.execute(
                    "INSERT INTO students VALUES (?, ?, ?)",
                    record
                )

                connection.execute("RELEASE SAVEPOINT one_record")

            except sqlite3.IntegrityError as error:
                connection.execute(
                    "ROLLBACK TO SAVEPOINT one_record"
                )
                connection.execute("RELEASE SAVEPOINT one_record")

                print("Rejected:", record, error)

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    print(connection.execute(
        "SELECT * FROM students"
    ).fetchall())

finally:
    connection.close()