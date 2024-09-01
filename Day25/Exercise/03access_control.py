# Exercise 3: Access Control

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age  # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        if isinstance(name, str) and name:
            self.__name = name
        else:
            print("Invalid name")

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age with validation
    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Invalid age")

person = Person("John", 25)
print(person.get_name())
person.set_age(30)
print(person.get_age())
