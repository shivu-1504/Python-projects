print("====== Library Management System ======")

BOOK_FILE = "books.txt"
ISSUE_FILE = "issued_books.txt"

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.book_id} | {self.title} | {self.author} | {status}"

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        books = []
        try:
            with open(BOOK_FILE, "r") as file:
                for line in file:
                    book_id, title, author, available = line.strip().split(",")
                    books.append(
                        Book(book_id, title, author, available == "True")
                    )
        except FileNotFoundError:
            pass
        return books

    def save_books(self):
        with open(BOOK_FILE, "w") as file:
            for book in self.books:
                file.write(
                    f"{book.book_id},{book.title},{book.author},{book.available}\n"
                )

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print("Book added successfully.")

    def issue_book(self, book_id, member):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    self.save_books()

                    with open(ISSUE_FILE, "a") as file:
                        file.write(
                            f"{book.book_id},{book.title},{member.member_id},{member.name}\n"
                        )

                    print("Book issued successfully.")
                    return
                else:
                    print("Book is already issued.")
                    return

        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    self.save_books()
                    print("Book returned successfully.")
                    return
                else:
                    print("Book was not issued.")
                    return

        print("Book not found.")

  
    def display_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book)


if __name__ == "__main__":

    library = Library()

    library.add_book(Book("1", "Python Basics", "Guido"))
    library.add_book(Book("2", "Data Structures", "Mark"))

    print("\nAll Books:")
    library.display_books()

    member1 = Member("M101", "Shiv")

    library.issue_book("1", member1)

    print("\nAfter Issuing:")
    library.display_books()

    library.return_book("1")

    print("\nAfter Returning:")
    library.display_books()