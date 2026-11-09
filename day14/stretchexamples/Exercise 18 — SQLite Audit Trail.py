'''
Exercise 18 — SQLite Audit Trail
'''

import sqlite3
from datetime import UTC, datetime

connection = sqlite3.connect(":memory:")

try:
    connection.execute("""
        CREATE TABLE audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT NOT NULL,
            entity_id TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

    connection.commit()

    def audit(action, entity_id):
        timestamp = datetime.now(UTC).isoformat()

        with connection:
            connection.execute(
                """
                INSERT INTO audit_logs
                (action, entity_id, timestamp)
                VALUES (?, ?, ?)
                """,
                (action, entity_id, timestamp)
            )

    audit("CREATE", "STUDENT101")
    audit("UPDATE", "STUDENT101")
    audit("DELETE", "STUDENT102")

    for row in connection.execute(
        "SELECT * FROM audit_logs ORDER BY id"
    ):
        print(row)

finally:
    connection.close()