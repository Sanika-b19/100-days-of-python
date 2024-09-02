# Exercise 1: Overload the ">" and "<" Operators

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 6)

print(f"Rectangle 1 is greater than Rectangle 2: {rect1 > rect2}")
print(f"Rectangle 1 is less than Rectangle 2: {rect1 < rect2}")
