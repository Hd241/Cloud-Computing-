import unittest
from business.services import LibraryService
from data.memory_repository import InMemoryBookRepository

class BusinessLogicTests(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryBookRepository()
        self.service = LibraryService(self.repo)

    def test_rejects_empty_title(self):
        with self.assertRaisesRegex(ValueError, "Title cannot be empty"):
            self.service.add_book("", "Author", "1234567890", 2020, 1)

    def test_rejects_empty_author(self):
        with self.assertRaisesRegex(ValueError, "Author cannot be empty"):
            self.service.add_book("Book", "", "1234567890", 2020, 1)

    def test_rejects_invalid_isbn(self):
        with self.assertRaisesRegex(ValueError, "ISBN"):
            self.service.add_book("Book", "Author", "123", 2020, 1)

    def test_rejects_future_year(self):
        from datetime import date
        with self.assertRaisesRegex(ValueError, "future"):
            self.service.add_book("Book", "Author", "1234567890", date.today().year + 1, 1)

    def test_rejects_negative_quantity(self):
        with self.assertRaisesRegex(ValueError, "negative"):
            self.service.add_book("Book", "Author", "1234567890", 2020, -1)

    def test_checkout_decreases_quantity(self):
        book = self.service.add_book("Book", "Author", "1234567890", 2020, 2)
        updated = self.service.check_out_book(book.id)
        self.assertEqual(updated.quantity, 1)

    def test_checkout_at_zero_returns_meaningful_error(self):
        book = self.service.add_book("Book", "Author", "1234567890", 2020, 0)
        with self.assertRaisesRegex(ValueError, "already 0"):
            self.service.check_out_book(book.id)

if __name__ == "__main__":
    unittest.main()
