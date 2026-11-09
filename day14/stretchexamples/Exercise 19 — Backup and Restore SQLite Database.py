'''
Exercise 19 — Backup and Restore SQLite Database
'''
import sqlite3
from pathlib import Path

source_path = Path("application.db")
backup_path = Path("application_backup.db")

with sqlite3.connect(source_path) as connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    with connection:
        connection.execute(
            """
            INSERT OR REPLACE INTO settings
            VALUES (?, ?)
            """,
            ("theme", "dark")
        )

with sqlite3.connect(source_path) as source, sqlite3.connect(backup_path) as backup:
    source.backup(backup)

with sqlite3.connect(backup_path) as restored:
    print(restored.execute(
        "SELECT * FROM settings"
    ).fetchall())

print("Backup exists:", backup_path.exists())