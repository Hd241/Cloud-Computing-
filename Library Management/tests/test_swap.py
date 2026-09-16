import tempfile, os
from business.services import LibraryService
from data.memory_repository import InMemoryBookRepository
from data.sqlite_repository import SQLiteBookRepository

def exercise(service):
    b = service.add_book("Clean Code", "Robert Martin", "1234567890123", 2008, 2)
    service.check_out_book(b.id)
    return service.get_book(b.id).quantity

def main():
    memory_result = exercise(LibraryService(InMemoryBookRepository()))
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    try:
        sqlite_result = exercise(LibraryService(SQLiteBookRepository(path)))
        print("Memory repository quantity:", memory_result)
        print("SQLite repository quantity:", sqlite_result)
        assert memory_result == sqlite_result == 1
        print("SWAP TEST PASSED: business logic used both data sources unchanged.")
    finally:
        os.remove(path)

if __name__ == "__main__":
    main()
