'''

Exercise 16 — Repository Pattern with Dependency Injection
'''
import sqlite3
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Student:
    id: int
    name: str


class StudentRepository(ABC):

    @abstractmethod
    def save(self, student):
        pass

    @abstractmethod
    def find(self, student_id):
        pass


class SQLiteStudentRepository(StudentRepository):

    def __init__(self, connection):
        self.connection = connection

        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)

    def save(self, student):
        self.connection.execute(
            "INSERT INTO students VALUES (?, ?)",
            (student.id, student.name)
        )

    def find(self, student_id):
        row = self.connection.execute(
            "SELECT id, name FROM students WHERE id = ?",
            (student_id,)
        ).fetchone()

        return Student(*row) if row else None


class StudentService:

    def __init__(self, repository):
        self.repository = repository

    def register(self, student):
        if self.repository.find(student.id):
            raise ValueError("Duplicate student")

        self.repository.save(student)


connection = sqlite3.connect(":memory:")

try:
    repository = SQLiteStudentRepository(connection)
    service = StudentService(repository)

    with connection:
        service.register(Student(101, "Alice"))

    print(repository.find(101))

finally:
    connection.close()