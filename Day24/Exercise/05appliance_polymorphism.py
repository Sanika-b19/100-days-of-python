# Exercise 5: Polymorphism with Appliances

class Appliance:
    def operate(self):
        pass

class WashingMachine(Appliance):
    def operate(self):
        return "Washing clothes"

class Refrigerator(Appliance):
    def operate(self):
        return "Cooling food"

class Microwave(Appliance):
    def operate(self):
        return "Heating food"

 
appliances = [WashingMachine(), Refrigerator(), Microwave()]

for appliance in appliances:
    print(appliance.operate())
