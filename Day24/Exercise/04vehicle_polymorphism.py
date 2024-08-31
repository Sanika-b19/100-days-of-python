# Exercise 4: Polymorphism with Vehicles

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving on the road"

class Bike(Vehicle):
    def move(self):
        return "Riding on the road"

class Truck(Vehicle):
    def move(self):
        return "Transporting goods on the road"
 
vehicles = [Car(), Bike(), Truck()]

for vehicle in vehicles:
    print(vehicle.move())
