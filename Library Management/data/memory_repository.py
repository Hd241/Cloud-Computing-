from business.models import Book
from business.repository import BookRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = {}
        self.next_id = 1

    def add(self, book):
        saved = Book(self.next_id, book.title, book.author, book.isbn,
                     book.publication_year, book.quantity)
        self.books[self.next_id] = saved
        self.next_id += 1
        return saved

    def get_all(self):
        return list(self.books.values())

    def get_by_id(self, book_id):
        return self.books.get(book_id)

    def update(self, book):
        if book.id not in self.books:
            raise KeyError("Book not found.")
        self.books[book.id] = book
        return book

    def delete(self, book_id):
        if book_id not in self.books:
            raise KeyError("Book not found.")
        del self.books[book_id]
