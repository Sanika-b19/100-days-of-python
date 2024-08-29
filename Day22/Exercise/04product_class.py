# Exercise 4: Create a Product Class with Methods

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        self.price = new_price

    def restock(self, amount):
        self.quantity += amount

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity in stock: {self.quantity}")

product = Product("Laptop", 999.99, 10)
product.update_price(949.99)
product.restock(5)
product.display()
