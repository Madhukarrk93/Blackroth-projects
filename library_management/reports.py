
"""Reporting features for the Library Management System."""

from typing import Any

from book import BookManager
from issue import IssueManager
from member import MemberManager


class LibraryReports:
    """Generate reports about books, borrowers, and fines."""

    def __init__(self) -> None:
        """Initialize the report dependencies."""
        self.book_manager = BookManager()
        self.member_manager = MemberManager()
        self.issue_manager = IssueManager()

    def available_books(self) -> list[dict[str, Any]]:
        """Return books that have at least one available copy."""
        return [
            book.to_dict()
            for book in self.book_manager.list_books()
            if book.available_copies > 0
        ]

    def borrowed_books(self) -> list[dict[str, Any]]:
        """Return currently active loans with book and member details."""
        active_issues = self.issue_manager.list_active_issues()
        books = {
            book.book_id: book
            for book in self.book_manager.list_books()
        }
        members = {
            member.member_id: member
            for member in self.member_manager.list_members()
        }

        results = []

        for issue in active_issues:
            book = books.get(issue["book_id"])
            member = members.get(issue["member_id"])

            results.append(
                {
                    **issue,
                    "book_title": book.title if book else "Unknown book",
                    "member_name": (
                        member.name if member else "Unknown member"
                    ),
                }
            )

        return results

    def top_borrowers(self, limit: int = 5) -> list[dict[str, Any]]:
        """Rank members by the number of books they have borrowed."""
        if isinstance(limit, bool) or not isinstance(limit, int) or limit < 1:
            raise ValueError("Limit must be a positive integer.")

        counts: dict[int, int] = {}

        for issue in self.issue_manager.list_issues():
            member_id = issue["member_id"]
            counts[member_id] = counts.get(member_id, 0) + 1

        members = {
            member.member_id: member
            for member in self.member_manager.list_members()
        }

        rankings = [
            {
                "member_id": member_id,
                "member_name": (
                    members[member_id].name
                    if member_id in members
                    else "Unknown member"
                ),
                "borrow_count": count,
            }
            for member_id, count in counts.items()
        ]

        return sorted(
            rankings,
            key=lambda item: item["borrow_count"],
            reverse=True,
        )[:limit]

    def total_fines(self) -> float:
        """Return the sum of fines recorded on all loan records."""
        return sum(
            float(issue.get("fine", 0.0))
            for issue in self.issue_manager.list_issues()
        )

    def summary(self) -> dict[str, Any]:
        """Return a summary of library activity."""
        books = self.book_manager.list_books()
        members = self.member_manager.list_members()
        issues = self.issue_manager.list_issues()

        return {
            "total_book_titles": len(books),
            "total_copies": sum(book.total_copies for book in books),
            "available_copies": sum(
                book.available_copies for book in books
            ),
            "registered_members": len(members),
            "total_issues": len(issues),
            "active_issues": len(
                self.issue_manager.list_active_issues()
            ),
            "total_fines": self.total_fines(),
        }
