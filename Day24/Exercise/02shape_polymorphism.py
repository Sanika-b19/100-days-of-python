# Exercise 2: Polymorphism with Shapes

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"

class Triangle(Shape):
    def draw(self):
        return "Drawing a Triangle"

 
shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    print(shape.draw())
