# Blackroth-projects
python tasks

# Library Management System

## Overview
A Python-based Library Management System demonstrating Object-Oriented Programming (OOP), modular design, input validation, exception handling, and JSON file storage.

## Features
- Add, update, delete, list, and search books.
- Register and list library members.
- Issue and return books.
- Calculate fines for late returns.
- Generate library reports and top-borrower rankings.
- Persist records using JSON files.
- Validate input and handle custom exceptions.

## Project Structure
```text
library_management/
├── app.py
├── book.py
├── member.py
├── issue.py
├── reports.py
├── storage.py
├── exceptions.py
├── validator.py
├── README.md
└── data/
    ├── books.json
    ├── members.json
    └── issues.json
```

## Requirements
- Python 3.10 or newer

No third-party packages are required.

## How to Run
Open a terminal in the `library_management` folder and run:

```bash
python app.py
```

Follow the on-screen menu to manage books, members, loans, and reports.

## Data Storage
The application stores books, members, and issue records in JSON files inside the `data` folder. Records persist between application runs.

## Concepts Demonstrated
- Classes and objects
- Encapsulation and composition
- Modular programming
- Type hints and docstrings
- Custom exceptions and validation
- JSON persistence
