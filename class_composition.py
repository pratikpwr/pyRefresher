# class composition is used when we need more instances of derived class


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Poter")
book2 = Book("Python 101")
print(book2)
self = BookShelf(book, book2)
print(self)
print(self.books)
