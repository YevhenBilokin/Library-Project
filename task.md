# Project: Library Management System

## Description:
The goal of this project is to build a simple Library Management System using Python. You will create classes for managing books, readers, and library staff. This project will help you practice object-oriented programming concepts like classes, objects, inheritance, polymorphism, encapsulation, and more.

## Requirements:

### 1. Classes to Create:
- **Book** class with the following attributes:
  - `title` (string)
  - `author` (string)
  - `year` (integer)
  - `is_available` (boolean, default `True`)

- **Reader** class with the following attributes:
  - `name` (string)
  - `borrowed_books` (list, starts as empty)

- **Library** class with the following attributes and methods:
  - `books` (list to store books)
  - `readers` (list to store readers)
  - `add_book(book)` (method to add books to the library)
  - `search_book(title)` (method to search for a book by title)
  - `borrow_book(book, reader)` (method to borrow a book for a reader)
  - `return_book(book, reader)` (method to return a book by a reader)

### 2. Inheritance and Polymorphism:
- Create **Ebook** and **PrintedBook** classes that inherit from `Book`.
- Implement a method `get_info()` in each subclass that returns the appropriate information about the book, such as "This is an eBook" or "This is a printed book".

### 3. Encapsulation:
- Make the `is_available` attribute in the `Book` class private and provide methods to check and update the availability status of the book.
- Use getter and setter methods for accessing and modifying the `borrowed_books` list in the `Reader` class.

### 4. Decorators:
- Implement a decorator for logging book borrowing and returning actions.
- Optionally, create a decorator to handle retry logic for finding a book in case it's not available.

### 5. User Interaction (Optional):
- Create a simple console-based interface or a GUI using `Tkinter` to allow users to interact with the system.
  - Allow users to:
    - Add books to the library
    - Borrow books
    - Return books
    - Search for books by title or author

## Example Code:

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

class Ebook(Book):
    def get_info(self):
        return f"{super().get_info()} - This is an eBook"

class PrintedBook(Book):
    def get_info(self):
        return f"{super().get_info()} - This is a printed book"

class Reader:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} has not borrowed {book.title}")

class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                return book
        return None

# Example usage
library = Library()
book1 = PrintedBook("Python Programming", "John Doe", 2021)
book2 = Ebook("Data Science for Beginners", "Jane Smith", 2022)
reader1 = Reader("Alice")

library.add_book(book1)
library.add_book(book2)

# Search and borrow books
found_book = library.search_book("Python Programming")
if found_book:
    reader1.borrow_book(found_book)

found_book = library.search_book("Data Science for Beginners")
if found_book:
    reader1.borrow_book(found_book)
