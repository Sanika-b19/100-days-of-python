# Exercise 3: Create a Library Book Class

class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
        else:
            print("The book is currently unavailable")

    def return_book(self):
        self.available = True

book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book.borrow()
print(f"Available: {book.available}")  # Output: Available: False
book.return_book()
print(f"Available: {book.available}")  # Output: Available: True
