
"""Book models and book management operations."""

from typing import Any

from exceptions import BookNotFoundError, ValidationError
from storage import JSONStorage
from validator import validate_non_empty, validate_positive_int


class Book:
    """Represent a book in the library."""

    def __init__(
        self,
        book_id: int,
        title: str,
        author: str,
        total_copies: int = 1,
        borrowed_copies: int = 0,
    ) -> None:
        """Initialize a book with its details."""
        self.book_id = validate_positive_int(book_id, "Book ID")
        self.title = validate_non_empty(title, "Title")
        self.author = validate_non_empty(author, "Author")
        self.total_copies = validate_positive_int(
            total_copies, "Total copies"
        )

        if (
            isinstance(borrowed_copies, bool)
            or not isinstance(borrowed_copies, int)
            or borrowed_copies < 0
            or borrowed_copies > self.total_copies
        ):
            raise ValidationError(
                "Borrowed copies must be between zero and total copies."
            )

        self.borrowed_copies = borrowed_copies

    @property
    def available_copies(self) -> int:
        """Return the number of copies currently available."""
        return self.total_copies - self.borrowed_copies

    def to_dict(self) -> dict[str, Any]:
        """Convert the book into a JSON-compatible dictionary."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "total_copies": self.total_copies,
            "borrowed_copies": self.borrowed_copies,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Book":
        """Create a book from a stored dictionary."""
        return cls(
            book_id=data["book_id"],
            title=data["title"],
            author=data["author"],
            total_copies=data.get("total_copies", 1),
            borrowed_copies=data.get("borrowed_copies", 0),
        )


class BookManager:
    """Manage the library's collection of books."""

    def __init__(self) -> None:
        """Initialize book management with JSON storage."""
        self.storage = JSONStorage("books.json")

    def _load_books(self) -> list[Book]:
        """Load all books from storage."""
        return [
            Book.from_dict(record)
            for record in self.storage.load()
        ]

    def _save_books(self, books: list[Book]) -> None:
        """Save all books to storage."""
        self.storage.save([book.to_dict() for book in books])

    def add_book(
        self,
        book_id: int,
        title: str,
        author: str,
        total_copies: int = 1,
    ) -> Book:
        """Add a new book to the collection."""
        books = self._load_books()

        if any(book.book_id == book_id for book in books):
            raise ValidationError(f"Book ID {book_id} already exists.")

        book = Book(book_id, title, author, total_copies)
        books.append(book)
        self._save_books(books)
        return book

    def get_book(self, book_id: int) -> Book:
        """Find a book by its ID."""
        for book in self._load_books():
            if book.book_id == book_id:
                return book

        raise BookNotFoundError(f"Book ID {book_id} was not found.")

    def search_books(self, query: str) -> list[Book]:
        """Search book titles and authors without case sensitivity."""
        query = validate_non_empty(query, "Search query").casefold()

        return [
            book
            for book in self._load_books()
            if query in book.title.casefold()
            or query in book.author.casefold()
        ]

    def update_book(
        self,
        book_id: int,
        title: str | None = None,
        author: str | None = None,
        total_copies: int | None = None,
    ) -> Book:
        """Update a book's details."""
        books = self._load_books()

        for book in books:
            if book.book_id == book_id:
                new_title = (
                    validate_non_empty(title, "Title")
                    if title is not None
                    else book.title
                )
                new_author = (
                    validate_non_empty(author, "Author")
                    if author is not None
                    else book.author
                )

                new_total = (
                    validate_positive_int(total_copies, "Total copies")
                    if total_copies is not None
                    else book.total_copies
                )

                if new_total < book.borrowed_copies:
                    raise ValidationError(
                        "Total copies cannot be fewer than borrowed copies."
                    )

                book.title = new_title
                book.author = new_author
                book.total_copies = new_total
                self._save_books(books)
                return book

        raise BookNotFoundError(f"Book ID {book_id} was not found.")

    def delete_book(self, book_id: int) -> None:
        """Delete a book if none of its copies are borrowed."""
        books = self._load_books()

        for book in books:
            if book.book_id == book_id:
                if book.borrowed_copies > 0:
                    raise ValidationError(
                        "Cannot delete a book while copies are borrowed."
                    )

                books.remove(book)
                self._save_books(books)
                return

        raise BookNotFoundError(f"Book ID {book_id} was not found.")

    def list_books(self) -> list[Book]:
        """Return all books in the collection."""
        return self._load_books()

    def change_borrowed_copies(
        self, book_id: int, change: int
    ) -> Book:
        """Adjust the borrowed-copy count when issuing or returning a book."""
        books = self._load_books()

        for book in books:
            if book.book_id == book_id:
                new_count = book.borrowed_copies + change

                if new_count < 0 or new_count > book.total_copies:
                    raise ValidationError(
                        "Borrowed-copy count would be invalid."
                    )

                book.borrowed_copies = new_count
                self._save_books(books)
                return book

        raise BookNotFoundError(f"Book ID {book_id} was not found.")
