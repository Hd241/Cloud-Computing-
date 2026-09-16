from business.services import LibraryService
from business.models import Book
from data.memory_repository import InMemoryBookRepository

def make_service():
    return LibraryService(InMemoryBookRepository())

def print_books(books):
    if not books:
        print("No books found.")
        return
    for b in books:
        print(f"{b.id}: {b.title} | {b.author} | ISBN {b.isbn} | {b.publication_year} | Qty {b.quantity}")

def main():
    service = make_service()
    print("Library Management - N-Tier Demo")
    while True:
        print("\n1 Add  2 View  3 Search  4 Update  5 Delete  6 Check out  7 Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                book = service.add_book(
                    input("Title: "), input("Author: "), input("ISBN: "),
                    int(input("Publication year: ")), int(input("Quantity: "))
                )
                print(f"Added book #{book.id}")
            elif choice == "2":
                print_books(service.get_all_books())
            elif choice == "3":
                print_books(service.search_books(input("Search title/author: ")))
            elif choice == "4":
                book_id = int(input("Book ID: "))
                current = service.get_book(book_id)
                if not current:
                    print("Book not found.")
                    continue
                title = input(f"Title [{current.title}]: ") or current.title
                author = input(f"Author [{current.author}]: ") or current.author
                isbn = input(f"ISBN [{current.isbn}]: ") or current.isbn
                year = input(f"Year [{current.publication_year}]: ")
                qty = input(f"Quantity [{current.quantity}]: ")
                service.update_book(book_id, title, author, isbn,
                                    int(year) if year else current.publication_year,
                                    int(qty) if qty else current.quantity)
                print("Updated.")
            elif choice == "5":
                service.delete_book(int(input("Book ID: ")))
                print("Deleted.")
            elif choice == "6":
                print(service.check_out_book(int(input("Book ID: "))))
            elif choice == "7":
                break
            else:
                print("Invalid choice.")
        except (ValueError, KeyError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
