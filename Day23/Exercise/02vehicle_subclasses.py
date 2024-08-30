# Exercise 2: Create a Vehicle Class and Subclasses

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def open_trunk(self):
        print("Trunk opened")

class Truck(Vehicle):
    def load_cargo(self, weight):
        print(f"Loaded {weight} kg of cargo")

car = Car("Toyota", "Camry", 2020)
truck = Truck("Ford", "F-150", 2018)
car.start_engine()  # Output: Engine started
truck.load_cargo(500)  # Output: Loaded 500 kg of cargo
