# Exercise 1: Implement Polymorphism with Animals

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.speak())
