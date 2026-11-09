'''
Exercise 17 — Idempotent Event Processing
'''

import sqlite3

connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
        CREATE TABLE events (
            event_id TEXT PRIMARY KEY,
            payload TEXT NOT NULL
        )
    """)

    connection.commit()

    def process_event(event_id, payload):
        with connection:
            cursor = connection.execute(
                """
                INSERT OR IGNORE INTO events
                (event_id, payload)
                VALUES (?, ?)
                """,
                (event_id, payload)
            )

            return cursor.rowcount == 1

    print(process_event("EVT101", "Order created"))
    print(process_event("EVT101", "Order created"))
    print(process_event("EVT102", "Payment received"))

    print(connection.execute(
        "SELECT * FROM events"
    ).fetchall())

finally:
    connection.close()