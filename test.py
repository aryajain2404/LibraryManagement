import json
import os

class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.loadBooks()

    def loadBooks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.books = json.load(file)
        else:
            self.books = []

    def saveBooks(self):
        with open(self.filename, "w") as file:
            json.dump(self.books, file, indent=4)

    def displayBooks(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable books in the library:")
            for book in self.books:
                status = "Available" if not book["borrowed"] else "Borrowed"
                print(f' * "{book["title"]}" by {book["author"]} ({book["year"]}) [ISBN: {book["isbn"]}] - {status}')

    def addBook(self, title, author, year, isbn):
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "isbn": isbn,
            "borrowed": False
        }
        self.books.append(new_book)
        self.saveBooks()
        print(f'Thank you! "{title}" has been added to the library.')

    def borrowBook(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if book["borrowed"]:
                    print(f'Sorry! "{title}" is already borrowed.')
                    return
                book["borrowed"] = True
                self.saveBooks()
                print(f'You have borrowed "{title}". Please handle it with care.')
                return
        print(f'Sorry! "{title}" not found in the library.')

    def returnBook(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if not book["borrowed"]:
                    print(f'"{title}" was not borrowed.')
                    return
                book["borrowed"] = False
                self.saveBooks()
                print(f'Thank you for returning "{title}".')
                return
        print(f'"{title}" not found in the library.')

    def searchBooks(self, keyword):
        results = []
        for book in self.books:
            if (keyword.lower() in book["title"].lower() or
                keyword.lower() in book["author"].lower() or
                keyword.lower() in str(book["year"])):
                results.append(book)

        if results:
            print("\nSearch results:")
            for book in results:
                status = "Available" if not book["borrowed"] else "Borrowed"
                print(f' * "{book["title"]}" by {book["author"]} ({book["year"]}) [ISBN: {book["isbn"]}] - {status}')
        else:
            print("No matching books found.")


class Student:
    def getBookDetails(self):
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        year = input("Enter Publication Year: ")
        isbn = input("Enter ISBN Number: ")
        return title, author, year, isbn

    def requestTitle(self, action="borrow"):
        return input(f"Enter the title of the book to {action}: ")

    def searchKeyword(self):
        return input("Enter keyword (title/author/year) to search: ")


if __name__ == "__main__":
    centralLibrary = Library()
    student = Student()

    while True:
        print("""
========= Welcome to the Central Library =========
1. List all books
2. Add a new book
3. Search for a book
4. Borrow a book
5. Return a book
6. Exit
        """)
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            centralLibrary.displayBooks()
        elif choice == "2":
            bookDetails = student.getBookDetails()
            centralLibrary.addBook(*bookDetails)
        elif choice == "3":
            keyword = student.searchKeyword()
            centralLibrary.searchBooks(keyword)
        elif choice == "4":
            title = student.requestTitle("borrow")
            centralLibrary.borrowBook(title)
        elif choice == "5":
            title = student.requestTitle("return")
            centralLibrary.returnBook(title)
        elif choice == "6":
            print("Thank you for using the Central Library. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
