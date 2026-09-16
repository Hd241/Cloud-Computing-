# Simple N-Tier Library Management Application

This project implements the assignment as a Python CLI application. It follows three distinct tiers: Presentation, Business, and Data. The assignment requires the architecture to be more important than the technology and requires add/view/search/update/delete/check-out functionality. [See the supplied assignment for the requirements.]

## Project structure

```text
library_n_tier/
├── presentation/
│   └── cli.py
├── business/
│   ├── models.py
│   ├── repository.py
│   └── services.py
├── data/
│   ├── memory_repository.py
│   └── sqlite_repository.py
├── tests/
│   ├── test_business.py
│   └── test_swap.py
├── ARCHITECTURE.md
└── README.md
```

## Architecture

```text
+---------------------------+
|   PRESENTATION TIER       |
| presentation/cli.py       |
| Input / output only       |
+-------------+-------------+
              |
              v
+---------------------------+
|     BUSINESS TIER         |
| business/services.py      |
| Validation + rules        |
| Depends on repository     |
| abstraction only          |
+-------------+-------------+
              |
              v
+---------------------------+
|       DATA TIER           |
| data/*_repository.py      |
| Persistence only          |
+-------------+-------------+
              |
       +------+------+
       |             |
       v             v
   In-memory      SQLite
```

Data flows downward for operations and results/errors flow back upward.

## What each tier does

### Presentation
`presentation/cli.py` collects user input, calls the business service, and prints results/errors. It does not contain validation rules or database calls.

### Business
`business/services.py` contains all required validation and business rules. It depends on `BookRepository`, an abstraction defined in `business/repository.py`, so it does not import SQLite or any database library.

### Data
`data/memory_repository.py` and `data/sqlite_repository.py` implement the repository abstraction. They only store and retrieve `Book` objects. Validation is deliberately kept out of these classes.

## Requirements implemented

- Add a book
- View all books
- Search by partial title or author
- Update any book field
- Delete by ID
- Check out a book
- Title and Author cannot be empty
- Publication year cannot be in the future
- ISBN must contain exactly 10 or 13 digits
- Quantity cannot be negative
- Checkout cannot reduce quantity below zero
- Meaningful business errors
- Seven business-layer unit tests using an in-memory fake data source
- SQLite and in-memory implementations
- Swap test proving the same business service works with both repositories

## How to run

Python 3.10+ is recommended.

From the project root:

```bash
python -m presentation.cli
```

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

Run the swap test:

```bash
python -m tests.test_swap
```

No third-party packages are required.

## Design decision

I used a repository interface (`BookRepository`) between the business and data tiers so the business logic is independent of the persistence mechanism. The same `LibraryService` can receive either `InMemoryBookRepository` or `SQLiteBookRepository`, which demonstrates loose coupling and makes business logic easy to test without a real database. This also keeps the presentation tier unaware of how books are stored.

## Error handling

Business validation raises `ValueError` with meaningful messages. Missing books raise `KeyError`. The presentation tier catches these expected errors and displays them instead of exposing a traceback to the user.

## Submission

Submit this project folder or its ZIP file containing the three required folders, tests, README, and architecture diagram.
