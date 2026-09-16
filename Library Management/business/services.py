from datetime import date
from .models import Book
from .repository import BookRepository

class LibraryService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def _validate(self, title, author, isbn, publication_year, quantity):
        if not str(title).strip():
            raise ValueError("Title cannot be empty.")
        if not str(author).strip():
            raise ValueError("Author cannot be empty.")
        if not str(isbn).isdigit() or len(str(isbn)) not in (10, 13):
            raise ValueError("ISBN must be exactly 10 or 13 digits.")
        if not isinstance(publication_year, int) or publication_year > date.today().year:
            raise ValueError("Publication Year must be a valid year and not in the future.")
        if publication_year < 1:
            raise ValueError("Publication Year must be a valid year.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity cannot be negative.")

    def add_book(self, title, author, isbn, publication_year, quantity):
        self._validate(title, author, isbn, publication_year, quantity)
        return self.repository.add(Book(None, title.strip(), author.strip(), str(isbn),
                                        publication_year, quantity))

    def get_all_books(self):
        return self.repository.get_all()

    def get_book(self, book_id):
        return self.repository.get_by_id(book_id)

    def search_books(self, term):
        term = term.lower().strip()
        return [b for b in self.repository.get_all()
                if term in b.title.lower() or term in b.author.lower()]

    def update_book(self, book_id, title, author, isbn, publication_year, quantity):
        if not self.repository.get_by_id(book_id):
            raise KeyError("Book not found.")
        self._validate(title, author, isbn, publication_year, quantity)
        return self.repository.update(Book(book_id, title.strip(), author.strip(), str(isbn),
                                           publication_year, quantity))

    def delete_book(self, book_id):
        if not self.repository.get_by_id(book_id):
            raise KeyError("Book not found.")
        self.repository.delete(book_id)

    def check_out_book(self, book_id):
        book = self.repository.get_by_id(book_id)
        if not book:
            raise KeyError("Book not found.")
        if book.quantity == 0:
            raise ValueError("Cannot check out the book: quantity is already 0.")
        updated = Book(book.id, book.title, book.author, book.isbn,
                       book.publication_year, book.quantity - 1)
        self.repository.update(updated)
        return updated
