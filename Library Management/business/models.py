from dataclasses import dataclass

@dataclass
class Book:
    id: int | None
    title: str
    author: str
    isbn: str
    publication_year: int
    quantity: int
