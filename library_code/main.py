class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.is_avalible = True

    #Метод для правильного вывода списка
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Ebook(Book):

    def get_info(self):
        return f"{super().get_info()} - Это електронная книга"

class PrintedBook(Book):
    def get_info(self):
        return f"{super().get_info()} - Это напечатаная книга"

class Reader:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []
    

class Library:
    def __init__(self):
        self.books_list = []
        self.readers_list = []

    #Function to add new book in library
    def add_book(self, book):
        if book:
            self.books_list.append(book)
            print(f"Книга '{book.title}' была успешно добавлена!")
        else:
            print("Ошибка, книга не обнаружена")

    #Function to find book in library list
    def search_book(self, title):
        for book in self.books_list:
            if book.title == title and book.is_avalible:
                return book
        return None

    #Function to borrow book
    def borrow_book(self, book_name, reader):
        for book in self.books_list:
            try:
                if book.title == book_name and book.is_avalible:
                    book.is_avalible = False
                    reader.borrowed_books.append(book)
                    print(f"Книга: {book.title} была взята {reader.name}")
            except:
                print("Книга не доступна")
    
    #Function to return book
    def return_book(self, book_name, reader):
        for book in self.books_list:
            if book.title == book_name and book.is_avalible == False:
                book.is_avalible = True
                reader.borrowed_books.remove(book)
                print(f"Книга: {book.title} была возвращена пользователем {reader.name}")
            else:
                print("Книга не найдена или не доступна")

    #Fix it
    def get_list(self):
        return self.books_list
            


"""
if __name__ == "__main__":
    library = Library()

    book1 = PrintedBook("Python Programming", "John Doe", 2021, )
    book2 = Ebook("Data Science for Beginners", "Jane Smith", 2022, )

    reader1 = Reader("Caya")

    library.add_book(book1)
    library.add_book(book2)

    found_book = library.search_book("Data Science for Beginners")
    print(found_book)

    library.borrow_book("Data Science for Beginners", reader1)

    library.return_book("Data Science for Beginners", reader1)
"""