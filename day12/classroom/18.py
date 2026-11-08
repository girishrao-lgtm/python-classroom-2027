'''
Example 18 — Magic Methods and Object Representation
'''

class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return (
            f"Book({self.title!r}, "
            f"{self.author!r}, {self.price!r})"
        )

    def __len__(self):
        return len(self.title)

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return (
            self.title == other.title
            and self.author == other.author
        )


book1 = Book("Python Deep Dive", "Alice", 500)
book2 = Book("Python Deep Dive", "Alice", 600)

print(str(book1))
print(repr(book1))
print(len(book1))
print(book1 == book2)