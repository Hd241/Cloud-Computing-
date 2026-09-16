from abc import ABC, abstractmethod
from typing import Optional
from .models import Book

class BookRepository(ABC):
    @abstractmethod
    def add(self, book: Book) -> Book: ...

    @abstractmethod
    def get_all(self) -> list[Book]: ...

    @abstractmethod
    def get_by_id(self, book_id: int) -> Optional[Book]: ...

    @abstractmethod
    def update(self, book: Book) -> Book: ...

    @abstractmethod
    def delete(self, book_id: int) -> None: ...
