'''
Example 20 — Repository Pattern with SQLite
'''

import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class Student:
    roll_number: int
    name: str
    marks: int


class StudentRepository:

    def __init__(self, connection):
        self.connection = connection

        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                roll_number INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                marks INTEGER NOT NULL
            )
        """)

    def save(self, student):
        self.connection.execute(
            """
            INSERT INTO students
            (roll_number, name, marks)
            VALUES (?, ?, ?)
            """,
            (
                student.roll_number,
                student.name,
                student.marks
            )
        )

    def find_by_id(self, roll_number):
        row = self.connection.execute(
            """
            SELECT roll_number, name, marks
            FROM students
            WHERE roll_number = ?
            """,
            (roll_number,)
        ).fetchone()

        return Student(*row) if row else None

    def find_all(self):
        rows = self.connection.execute(
            "SELECT roll_number, name, marks FROM students"
        ).fetchall()

        return [Student(*row) for row in rows]


connection = sqlite3.connect(":memory:")

try:
    repository = StudentRepository(connection)

    with connection:
        repository.save(Student(101, "Alice", 90))
        repository.save(Student(102, "Bob", 85))

    print(repository.find_by_id(101))
    print(repository.find_all())

finally:
    connection.close()