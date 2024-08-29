# Exercise 2: Create a Circle Class with Methods

import math

class Circle:
    def __init__(self, radius, color="red"):
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def display(self):
        print(f"Circle with radius {self.radius} and color {self.color}")
        print(f"Area: {self.area():.2f}")
        print(f"Circumference: {self.circumference():.2f}")

circle = Circle(5, "blue")
circle.display()
