'''
Exercise 16 — Library Management System
'''

from dataclasses import dataclass


@dataclass
class Book:
    book_id: int
    title: str
    available: bool = True


class Library:

    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.book_id in self.books:
            raise ValueError("Duplicate book ID")

        self.books[book.book_id] = book

    def issue_book(self, book_id):
        book = self.books.get(book_id)

        if book is None:
            raise KeyError("Book not found")

        if not book.available:
            raise ValueError("Book already issued")

        book.available = False

    def return_book(self, book_id):
        book = self.books.get(book_id)

        if book is None:
            raise KeyError("Book not found")

        if book.available:
            raise ValueError("Book was not issued")

        book.available = True

    def available_books(self):
        return [
            book for book in self.books.values()
            if book.available
        ]


library = Library()

library.add_book(Book(101, "Python"))
library.add_book(Book(102, "Algorithms"))

library.issue_book(101)

print(library.available_books())

library.return_book(101)

print(library.available_books())