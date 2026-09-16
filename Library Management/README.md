# Simple N-Tier Library Management Application

It follows three distinct tiers: Presentation, Business, and Data. 

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


