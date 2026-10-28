
"""JSON storage utilities for the Library Management System."""

import json
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).parent / "data"


class JSONStorage:
    """Load and save records in JSON files."""

    def __init__(self, filename: str) -> None:
        """Initialize storage for a JSON file."""
        self.file_path = DATA_DIR / filename
        DATA_DIR.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            self.save([])

    def load(self) -> list[dict[str, Any]]:
        """Load records from a JSON file."""
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON data in {self.file_path.name}."
            ) from exc

        if not isinstance(data, list):
            raise ValueError(
                f"{self.file_path.name} must contain a JSON list."
            )

        return data

    def save(self, records: list[dict[str, Any]]) -> None:
        """Save records to a JSON file."""
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4, ensure_ascii=False)
