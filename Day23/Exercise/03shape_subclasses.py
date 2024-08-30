# Exercise 3: Create a Shape Class and Subclasses

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print(circle.area())  # Output: 78.53981633974483
print(circle.perimeter())  # Output: 31.41592653589793
