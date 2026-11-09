'''
Example 18 — SQLite Database Fundamentals
'''

import sqlite3

with sqlite3.connect("students.db") as connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_number INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            marks INTEGER NOT NULL
                CHECK (marks BETWEEN 0 AND 100)
        )
    """)

    connection.execute("DELETE FROM students")

    connection.executemany(
        "INSERT INTO students VALUES (?, ?, ?)",
        [
            (101, "Alice", 90),
            (102, "Bob", 85),
            (103, "Charlie", 95)
        ]
    )

    rows = connection.execute(
        "SELECT * FROM students ORDER BY marks DESC"
    ).fetchall()

for row in rows:
    print(row)