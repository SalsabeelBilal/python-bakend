class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Borrowed: {self.title}")
        else:
            print(f"Sorry, {self.title} is already borrowed.")

    def return_book(self):
        self.is_available = True
        print(f"Returned: {self.title}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def list_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"{book.title} by {book.author} - {status}")


if __name__ == "__main__":
    library = Library()
    b1 = Book("1984", "George Orwell")
    b2 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    library.add_book(b1)
    library.add_book(b2)
    library.list_books()

    b1.borrow()
    library.list_books()

    b1.return_book()
    library.list_books()
