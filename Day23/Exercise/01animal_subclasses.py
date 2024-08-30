# Exercise 1: Create an Animal Class and Subclasses

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Rex", 5)
cat = Cat("Whiskers", 3)
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
