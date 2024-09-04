# Exercise 1: Abstract Vehicle Class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def fuel_efficiency(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

    def stop_engine(self):
        return "Car engine stopped."

    def fuel_efficiency(self):
        return "Fuel efficiency: 25 MPG"

class Truck(Vehicle):
    def start_engine(self):
        return "Truck engine started."

    def stop_engine(self):
        return "Truck engine stopped."

    def fuel_efficiency(self):
        return "Fuel efficiency: 15 MPG"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started."

    def stop_engine(self):
        return "Motorcycle engine stopped."

    def fuel_efficiency(self):
        return "Fuel efficiency: 50 MPG"
 
vehicles = [Car(), Truck(), Motorcycle()]
for vehicle in vehicles:
    print(vehicle.start_engine())
    print(vehicle.fuel_efficiency())
    print(vehicle.stop_engine())
