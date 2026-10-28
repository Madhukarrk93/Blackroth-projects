
"""Main menu for the Library Management System."""

from book import BookManager
from exceptions import LibraryError
from issue import IssueManager
from member import MemberManager
from reports import LibraryReports


def show_menu() -> None:
    """Display the main menu."""
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add a book")
    print("2. List all books")
    print("3. Search books")
    print("4. Update a book")
    print("5. Delete a book")
    print("6. Add a member")
    print("7. List all members")
    print("8. Issue a book")
    print("9. Return a book")
    print("10. View reports")
    print("0. Exit")


def add_book(manager: BookManager) -> None:
    """Add a book to the library."""
    book_id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    copies = int(input("Enter total copies: "))

    book = manager.add_book(book_id, title, author, copies)
    print(f"Book added successfully: {book.title}")


def list_books(manager: BookManager) -> None:
    """Display all books."""
    books = manager.list_books()

    if not books:
        print("No books found.")
        return

    for book in books:
        print(
            f"ID: {book.book_id} | Title: {book.title} | "
            f"Author: {book.author} | Total: {book.total_copies} | "
            f"Available: {book.available_copies}"
        )


def search_books(manager: BookManager) -> None:
    """Search for books by title or author."""
    query = input("Enter title or author to search: ")
    books = manager.search_books(query)

    if not books:
        print("No matching books found.")
        return

    for book in books:
        print(f"{book.book_id}: {book.title} by {book.author}")


def update_book(manager: BookManager) -> None:
    """Update a book's details."""
    book_id = int(input("Enter book ID to update: "))
    title = input("New title (leave blank to keep current): ").strip()
    author = input("New author (leave blank to keep current): ").strip()
    copies_text = input(
        "New total copies (leave blank to keep current): "
    ).strip()

    book = manager.update_book(
        book_id,
        title=title or None,
        author=author or None,
        total_copies=int(copies_text) if copies_text else None,
    )
    print(f"Book updated successfully: {book.title}")


def delete_book(manager: BookManager) -> None:
    """Delete a book from the library."""
    book_id = int(input("Enter book ID to delete: "))
    manager.delete_book(book_id)
    print("Book deleted successfully.")


def add_member(manager: MemberManager) -> None:
    """Register a new member."""
    member_id = int(input("Enter member ID: "))
    name = input("Enter member name: ")
    email = input("Enter member email: ")

    member = manager.add_member(member_id, name, email)
    print(f"Member added successfully: {member.name}")


def list_members(manager: MemberManager) -> None:
    """Display all registered members."""
    members = manager.list_members()

    if not members:
        print("No members found.")
        return

    for member in members:
        print(
            f"ID: {member.member_id} | Name: {member.name} | "
            f"Email: {member.email}"
        )


def issue_book(manager: IssueManager) -> None:
    """Issue an available book to a member."""
    issue_id = int(input("Enter new issue ID: "))
    book_id = int(input("Enter book ID: "))
    member_id = int(input("Enter member ID: "))

    issue = manager.issue_book(issue_id, book_id, member_id)
    print(
        f"Book issued successfully. Due date: {issue['due_date']}"
    )


def return_book(manager: IssueManager) -> None:
    """Return a borrowed book."""
    issue_id = int(input("Enter issue ID to return: "))
    issue = manager.return_book(issue_id)

    print(f"Book returned successfully. Fine: ₹{issue['fine']:.2f}")


def show_reports(reports: LibraryReports) -> None:
    """Display library summary reports."""
    summary = reports.summary()

    print("\n===== LIBRARY REPORTS =====")
    for name, value in summary.items():
        print(f"{name.replace('_', ' ').title()}: {value}")

    print("\nTop borrowers:")
    borrowers = reports.top_borrowers()

    if not borrowers:
        print("No borrowing history found.")
    else:
        for borrower in borrowers:
            print(
                f"{borrower['member_name']}: "
                f"{borrower['borrow_count']} borrow(s)"
            )


def main() -> None:
    """Run the library management application."""
    books = BookManager()
    members = MemberManager()
    issues = IssueManager()
    reports = LibraryReports()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                add_book(books)
            elif choice == "2":
                list_books(books)
            elif choice == "3":
                search_books(books)
            elif choice == "4":
                update_book(books)
            elif choice == "5":
                delete_book(books)
            elif choice == "6":
                add_member(members)
            elif choice == "7":
                list_members(members)
            elif choice == "8":
                issue_book(issues)
            elif choice == "9":
                return_book(issues)
            elif choice == "10":
                show_reports(reports)
            elif choice == "0":
                print("Thank you for using the Library Management System!")
                break
            else:
                print("Invalid option. Please choose from the menu.")

        except (ValueError, LibraryError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()


