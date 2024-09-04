# Exercise 4: Abstract Shape with Area Calculation

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def calculate_volume(self):
        pass

class Cube(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return 6 * (self.side_length ** 2)

    def calculate_volume(self):
        return self.side_length ** 3

class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    def calculate_volume(self):
        return (4/3) * math.pi * (self.radius ** 3)
 
shapes = [Cube(3), Sphere(5)]
for shape in shapes:
    print(f"{shape.__class__.__name__} - Area: {shape.area():.2f}, Volume: {shape.calculate_volume():.2f}")
