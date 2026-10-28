
"""Demonstrate Python magic methods and operator overloading."""


class Book:
    """Represent a book and demonstrate common magic methods."""

    def __init__(self, title: str, pages: int) -> None:
        if not title.strip():
            raise ValueError("Book title cannot be empty.")
        if pages < 0:
            raise ValueError("Pages cannot be negative.")

        self.title = title
        self.pages = pages

    def __str__(self) -> str:
        """Return a user-friendly book description."""
        return f"{self.title} ({self.pages} pages)"

    def __repr__(self) -> str:
        """Return an unambiguous representation."""
        return f"Book(title={self.title!r}, pages={self.pages!r})"

    def __len__(self) -> int:
        """Return the number of pages."""
        return self.pages

    def __eq__(self, other: object) -> bool:
        """Books are equal when their titles and page counts match."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.pages == other.pages

    def __lt__(self, other: "Book") -> bool:
        """Compare books by page count."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __gt__(self, other: "Book") -> bool:
        """Compare books by page count."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages > other.pages

    def __add__(self, other: "Book") -> int:
        """Return the combined page count of two books."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages + other.pages

    def __sub__(self, other: "Book") -> int:
        """Return the difference between two books' page counts."""
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages - other.pages


def main() -> None:
    """Run examples of all implemented magic methods."""
    book1 = Book("Python Basics", 200)
    book2 = Book("Learning OOP", 300)
    book3 = Book("Python Basics", 200)

    print("1. __str__")
    print(book1)

    print("\n2. __repr__")
    print(repr(book1))

    print("\n3. __len__")
    print(len(book1))

    print("\n4. __eq__")
    print(book1 == book3)

    print("\n5. __lt__ and __gt__")
    print(book1 < book2)
    print(book2 > book1)

    print("\n6. __add__")
    print(book1 + book2)

    print("\n7. __sub__")
    print(book2 - book1)


if __name__ == "__main__":
    main()
