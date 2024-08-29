# Exercise 1: Create a Book Class with Methods

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount):
        self.price -= self.price * (discount / 100)

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

book = Book("Python Programming", "John Smith", 39.99)
book.apply_discount(10)
book.display_details()  # Output: Price: $35.99
