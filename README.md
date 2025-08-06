# LibraryManagement
A Simple command-line-based system to manage a library’s book collection. This system will operate locally and allow users to perform essential operations such as adding, viewing, searching, and borrowing/returning books. The goal is to apply object-oriented programming principles along with file-based data persistence.

This is a **Library Management System** built using Python. The system provides basic functionality for managing a library's books and users. It runs through the command line and allows users to perform operations such as adding books, borrowing books, returning books, viewing available books and also save data in the form of book.txt.

## Features

- **Add Books**: Add new books to the library collection.
- **ListAll Books**: List all available books in the library.
- **Borrow Books**: Borrow books from the library (updates book availability).
- **Return Books**: Return borrowed books to the library.
- **Save and Load Data**: Store book data in a file books.txt.

- ## Requirements
To run this program, you need:
- Python 3.x installed on your system.
- A terminal or command line interface.

## How to Run

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Run the Python file using the command:
   ```bash
   python test.py
   ```
4. Follow the prompts in the command line to interact with the Library Management System.
## Example Output

Here’s an example of what the command-line interface might look like:

```
========= Welcome to the Central Library =========
1. List all books
2. Add a new book
3. Search for a book
4. Borrow a book
5. Return a book
6. Exit

        
Enter your choice (1-6): 1

Available books in the library:
 * "The palace of illusion" by chitra banerjee (2008) [ISBN: 9789386215963] - Available
 * "I DON'T LOVE YOU ANYMORE" by RITHVIK SINGH (2024) [ISBN: 9798892772280] - Available
 * "GET EPIC SHIT DONE" by ANKUR WARIKOO (2022) [ISBN: 9789393986078] - Borrowed

========= Welcome to the Central Library =========
1. List all books
2. Add a new book
3. Search for a book
4. Borrow a book
5. Return a book
6. Exit

Enter your choice (1-6): 4
Enter the title of the book to borrow: get epic shit done
Sorry! "get epic shit done" is already borrowed.

Enter your choice (1-6): 1

Available books in the library:
 * "The palace of illusion" by chitra banerjee (2008) [ISBN: 9789386215963] - Available
 * "I DON'T LOVE YOU ANYMORE" by RITHVIK SINGH (2024) [ISBN: 9798892772280] - Available
 * "GET EPIC SHIT DONE" by ANKUR WARIKOO (2022) [ISBN: 9789393986078] - Borrowed

Enter your choice (1-6): 6
Thank you for using the Central Library. Goodbye!
