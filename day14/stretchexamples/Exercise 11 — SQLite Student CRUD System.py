'''
Exercise 11 — SQLite Student CRUD System
'''

import sqlite3

connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
        CREATE TABLE students (
            roll_number INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            marks INTEGER NOT NULL
        )
    """)

    with connection:
        connection.executemany(
            "INSERT INTO students VALUES (?, ?, ?)",
            [
                (101, "Alice", 90),
                (102, "Bob", 85),
                (103, "Charlie", 95)
            ]
        )

    print("Initial records:")
    print(connection.execute(
        "SELECT * FROM students"
    ).fetchall())

    with connection:
        connection.execute(
            "UPDATE students SET marks = ? WHERE roll_number = ?",
            (98, 101)
        )

        connection.execute(
            "DELETE FROM students WHERE roll_number = ?",
            (102,)
        )

    print("Updated records:")
    print(connection.execute(
        "SELECT * FROM students"
    ).fetchall())

finally:
    connection.close()