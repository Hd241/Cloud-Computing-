import sqlite3
from business.models import Book
from business.repository import BookRepository

class SQLiteBookRepository(BookRepository):
    def __init__(self, db_path="library.db"):
        self.db_path = db_path
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL, author TEXT NOT NULL, isbn TEXT NOT NULL,
                publication_year INTEGER NOT NULL, quantity INTEGER NOT NULL
            )""")

    def add(self, book):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(
                "INSERT INTO books(title,author,isbn,publication_year,quantity) VALUES(?,?,?,?,?)",
                (book.title, book.author, book.isbn, book.publication_year, book.quantity))
            return Book(cur.lastrowid, book.title, book.author, book.isbn,
                        book.publication_year, book.quantity)

    def get_all(self):
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute("SELECT id,title,author,isbn,publication_year,quantity FROM books").fetchall()
        return [Book(*r) for r in rows]

    def get_by_id(self, book_id):
        with sqlite3.connect(self.db_path) as conn:
            r = conn.execute("SELECT id,title,author,isbn,publication_year,quantity FROM books WHERE id=?",
                             (book_id,)).fetchone()
        return Book(*r) if r else None

    def update(self, book):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""UPDATE books SET title=?,author=?,isbn=?,publication_year=?,quantity=?
                            WHERE id=?""",
                         (book.title, book.author, book.isbn, book.publication_year, book.quantity, book.id))
        return book

    def delete(self, book_id):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM books WHERE id=?", (book_id,))
