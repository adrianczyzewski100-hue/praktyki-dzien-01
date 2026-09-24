class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        book = [book_id, title, author]
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(f"Tytul: {book[1]}, autor: {book[2]}")

    def find_by_id(self, book_id):
        for book in self.books:
            if book[0] == book_id:
                return book

    def remove_by_id(self, book_id):
        for book in self.books:
            if book[0] == book_id:
                self.books.remove(book)
                return True
        return False


library = Library()

library.add_book(2, "Pan Tadeusz", "Adam Mickiewicz")
library.add_book(1, "Lalka", "Boleslaw Prus")


print(library.remove_by_id(5))

library.show_books()