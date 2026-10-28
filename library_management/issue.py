
"""Book issuing, returning, and late-fine management."""

from datetime import date, timedelta
from typing import Any

from book import BookManager
from exceptions import (
    BookUnavailableError,
    IssueNotFoundError,
    MemberNotFoundError,
    ValidationError,
)
from member import MemberManager
from storage import JSONStorage
from validator import validate_positive_int


LOAN_DAYS = 14
DAILY_FINE = 5.0


class IssueManager:
    """Manage book loans and returns."""

    def __init__(self) -> None:
        """Initialize issue storage and related managers."""
        self.storage = JSONStorage("issues.json")
        self.book_manager = BookManager()
        self.member_manager = MemberManager()

    def _load_issues(self) -> list[dict[str, Any]]:
        """Load all issue records."""
        return self.storage.load()

    def _save_issues(self, issues: list[dict[str, Any]]) -> None:
        """Save issue records."""
        self.storage.save(issues)

    def issue_book(
        self,
        issue_id: int,
        book_id: int,
        member_id: int,
    ) -> dict[str, Any]:
        """Issue an available book to a registered member."""
        validate_positive_int(issue_id, "Issue ID")
        validate_positive_int(book_id, "Book ID")
        validate_positive_int(member_id, "Member ID")

        issues = self._load_issues()

        if any(issue["issue_id"] == issue_id for issue in issues):
            raise ValidationError(f"Issue ID {issue_id} already exists.")

        book = self.book_manager.get_book(book_id)
        self.member_manager.get_member(member_id)

        if book.available_copies <= 0:
            raise BookUnavailableError(
                f"Book '{book.title}' is not available."
            )

        issue_date = date.today()
        due_date = issue_date + timedelta(days=LOAN_DAYS)

        record = {
            "issue_id": issue_id,
            "book_id": book_id,
            "member_id": member_id,
            "issue_date": issue_date.isoformat(),
            "due_date": due_date.isoformat(),
            "return_date": None,
            "fine": 0.0,
        }

        # Update book availability and persist the loan.
        self.book_manager.change_borrowed_copies(book_id, 1)
        try:
            issues.append(record)
            self._save_issues(issues)
        except Exception:
            # Roll back the borrowed-copy count if saving fails.
            self.book_manager.change_borrowed_copies(book_id, -1)
            raise

        return record

    def return_book(
        self,
        issue_id: int,
        return_date: date | None = None,
    ) -> dict[str, Any]:
        """Return a loan and calculate any late-return fine."""
        validate_positive_int(issue_id, "Issue ID")
        actual_return_date = return_date or date.today()
        issues = self._load_issues()

        for issue in issues:
            if issue["issue_id"] != issue_id:
                continue

            if issue["return_date"] is not None:
                raise ValidationError("This book has already been returned.")

            due_date = date.fromisoformat(issue["due_date"])
            days_late = max((actual_return_date - due_date).days, 0)
            fine = days_late * DAILY_FINE

            issue["return_date"] = actual_return_date.isoformat()
            issue["fine"] = fine
            self._save_issues(issues)

            self.book_manager.change_borrowed_copies(
                issue["book_id"], -1
            )

            return issue

        raise IssueNotFoundError(
            f"Issue record {issue_id} was not found."
        )

    def list_issues(self) -> list[dict[str, Any]]:
        """Return all loan records."""
        return self._load_issues()

    def list_active_issues(self) -> list[dict[str, Any]]:
        """Return loans that have not yet been returned."""
        return [
            issue
            for issue in self._load_issues()
            if issue["return_date"] is None
        ]

    def get_member_fines(self, member_id: int) -> float:
        """Calculate the total fines recorded for a member."""
        validate_positive_int(member_id, "Member ID")
        self.member_manager.get_member(member_id)

        return sum(
            float(issue.get("fine", 0.0))
            for issue in self._load_issues()
            if issue["member_id"] == member_id
        )

