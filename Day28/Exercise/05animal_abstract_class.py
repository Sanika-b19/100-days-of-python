# Exercise 5: Abstract Animal Class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

    def move(self):
        return "Run"

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

    def move(self):
        return "Fly"

class Fish(Animal):
    def make_sound(self):
        return "Blub"

    def move(self):
        return "Swim"
 
animals = [Dog(), Bird(), Fish()]
for animal in animals:
    print(f"{animal.__class__.__name__} - Sound: {animal.make_sound()}, Movement: {animal.move()}")
