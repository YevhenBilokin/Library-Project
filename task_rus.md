# Проект: Система управления библиотекой

## Описание:
Цель этого проекта — построить простую систему управления библиотекой на Python. Вам нужно будет создать классы для управления книгами, читателями и библиотечным персоналом. Этот проект поможет вам попрактиковаться в применении концепций объектно-ориентированного программирования, таких как классы, объекты, наследование, полиморфизм, инкапсуляция и другие.

## Требования:

### 1. Классы для создания:
- Класс **Book** с атрибутами:
  - `title` (строка)
  - `author` (строка)
  - `year` (целое число)
  - `is_available` (булевое значение, по умолчанию `True`)

- Класс **Reader** с атрибутами:
  - `name` (строка)
  - `borrowed_books` (список, изначально пустой)

- Класс **Library** с атрибутами и методами:
  - `books` (список для хранения книг)
  - `readers` (список для хранения читателей)
  - `add_book(book)` (метод для добавления книги в библиотеку)
  - `search_book(title)` (метод для поиска книги по названию)
  - `borrow_book(book, reader)` (метод для выдачи книги читателю)
  - `return_book(book, reader)` (метод для возврата книги)

### 2. Наследование и полиморфизм:
- Создайте классы **Ebook** и **PrintedBook**, которые будут наследовать от класса `Book`.
- Реализуйте метод `get_info()` в каждом из подклассов, который будет возвращать соответствующую информацию о книге, например: "Это электронная книга" или "Это печатная книга".

### 3. Инкапсуляция:
- Сделайте атрибут `is_available` в классе `Book` закрытым и предоставьте методы для проверки и изменения его значения.
- Используйте геттеры и сеттеры для доступа и изменения списка `borrowed_books` в классе `Reader`.

### 4. Декораторы:
- Реализуйте декоратор для логирования операций с книгами (выдача и возврат).
- Опционально создайте декоратор для повторных попыток поиска книги в случае, если она недоступна.

### 5. Взаимодействие с пользователем (опционально):
- Создайте простое консольное приложение или GUI с использованием `Tkinter` для взаимодействия с системой.
  - Пользователи должны иметь возможность:
    - Добавлять книги в библиотеку
    - Заимствовать книги
    - Возвращать книги
    - Искать книги по названию или автору

## Пример кода:

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

# Пример использования
library = Library()
book1 = PrintedBook("Python Programming", "John Doe", 2021)
book2 = Ebook("Data Science for Beginners", "Jane Smith", 2022)
reader1 = Reader("Alice")

library.add_book(book1)
library.add_book(book2)

# Поиск и заимствование книг
found_book = library.search_book("Python Programming")
if found_book:
    reader1.borrow_book(found_book)

found_book = library.search_book("Data Science for Beginners")
if found_book:
    reader1.borrow_book(found_book)
