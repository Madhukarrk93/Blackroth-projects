"""Member models and member management operations."""

from typing import Any

from exceptions import MemberNotFoundError, ValidationError
from storage import JSONStorage
from validator import validate_email, validate_non_empty, validate_positive_int


class Member:
    """Represent a library member."""

    def __init__(
        self,
        member_id: int,
        name: str,
        email: str,
    ) -> None:
        """Initialize a library member."""
        self.member_id = validate_positive_int(member_id, "Member ID")
        self.name = validate_non_empty(name, "Name")
        self.email = validate_email(email)

    def to_dict(self) -> dict[str, Any]:
        """Convert the member into a JSON-compatible dictionary."""
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Member":
        """Create a member from stored data."""
        return cls(
            member_id=data["member_id"],
            name=data["name"],
            email=data["email"],
        )


class MemberManager:
    """Manage library members."""

    def __init__(self) -> None:
        """Initialize member management with JSON storage."""
        self.storage = JSONStorage("members.json")

    def _load_members(self) -> list[Member]:
        """Load all members from storage."""
        return [
            Member.from_dict(record)
            for record in self.storage.load()
        ]

    def _save_members(self, members: list[Member]) -> None:
        """Save all members to storage."""
        self.storage.save([member.to_dict() for member in members])

    def add_member(
        self,
        member_id: int,
        name: str,
        email: str,
    ) -> Member:
        """Add a new member."""
        members = self._load_members()

        if any(member.member_id == member_id for member in members):
            raise ValidationError(
                f"Member ID {member_id} already exists."
            )

        member = Member(member_id, name, email)
        members.append(member)
        self._save_members(members)
        return member

    def get_member(self, member_id: int) -> Member:
        """Find a member by ID."""
        for member in self._load_members():
            if member.member_id == member_id:
                return member

        raise MemberNotFoundError(
            f"Member ID {member_id} was not found."
        )

    def search_members(self, query: str) -> list[Member]:
        """Search members by name or email."""
        query = validate_non_empty(query, "Search query").casefold()

        return [
            member
            for member in self._load_members()
            if query in member.name.casefold()
            or query in member.email.casefold()
        ]

    def update_member(
        self,
        member_id: int,
        name: str | None = None,
        email: str | None = None,
    ) -> Member:
        """Update a member's details."""
        members = self._load_members()

        for member in members:
            if member.member_id == member_id:
                if name is not None:
                    member.name = validate_non_empty(name, "Name")

                if email is not None:
                    member.email = validate_email(email)

                self._save_members(members)
                return member

        raise MemberNotFoundError(
            f"Member ID {member_id} was not found."
        )

    def delete_member(self, member_id: int) -> None:
        """Delete a member."""
        members = self._load_members()

        for member in members:
            if member.member_id == member_id:
                members.remove(member)
                self._save_members(members)
                return

        raise MemberNotFoundError(
            f"Member ID {member_id} was not found."
        )

    def list_members(self) -> list[Member]:
        """Return all registered members."""
        return self._load_members()
