# Exercise 4: Create a Car Class

class Car:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, miles):
        self.mileage += miles

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}, Mileage: {self.mileage}")

car = Car("Toyota", "Camry", 2020)
car.drive(150)
car.display_info()  # Output: 2020 Toyota Camry, Mileage: 150
