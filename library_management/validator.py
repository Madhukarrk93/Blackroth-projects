
"""Input validation helpers for the Library Management System."""

from exceptions import ValidationError


def validate_non_empty(value: str, field_name: str) -> str:
    """Validate a required text field and return its cleaned value."""
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{field_name} cannot be empty.")
    return value.strip()


def validate_positive_int(value: int, field_name: str) -> int:
    """Validate that a value is a positive integer."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValidationError(f"{field_name} must be a positive integer.")
    return value


def validate_email(email: str) -> str:
    """Perform basic email address validation."""
    email = validate_non_empty(email, "Email")

    if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        raise ValidationError("Please enter a valid email address.")

    return email
