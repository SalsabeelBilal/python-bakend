class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} ({self.year}) - {status}"


class Library:

    def __init__(self, name):
        self.name = name
        self.__books = []  # Private list of books

    def add_book(self, book):
        self.__books.append(book)
        print(f"'{book.title}' added to the library.")

    def remove_book(self, title):
        for book in self.__books:
            if book.title.lower() == title.lower():
                self.__books.remove(book)
                print(f" '{book.title}' removed from the library.")
                return
        print(f" Book '{title}' not found.")

    def borrow_book(self, title):
        for book in self.__books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"📖 You borrowed '{book.title}'.")
                    return
                else:
                    print(f" '{book.title}' is already checked out.")
                    return
        print(f"Book '{title}' not found.")

    def return_book(self, title):
        for book in self.__books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f" You returned '{book.title}'.")
                    return
                else:
                    print(f" '{book.title}' was not borrowed.")
                    return
        print(f"Book '{title}' not found.")

    def search_books(self, keyword):
        results = [book for book in self.__books
                   if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if results:
            print(f"🔍 Search results for '{keyword}':")
            for b in results:
                print(f"   - {b}")
        else:
            print(f" No books found for '{keyword}'.")

    def display_books(self):
        if self.__books:
            print(f" {self.name} Library Collection:")
            for book in self.__books:
                print(f"   - {book}")
        else:
            print("The library is empty.")



if __name__ == "__main__":
 
    my_library = Library("Central")

  
    my_library.add_book(Book("1984", "George Orwell", 1949))
    my_library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))

   
    my_library.display_books()

    
    my_library.search_books("George")

    
    my_library.borrow_book("1984")
    my_library.borrow_book("1984")  
    my_library.return_book("1984")


    my_library.remove_book("The Great Gatsby")
    my_library.display_books()
