# Project: Implement Encapsulation in Your Student Class

class Student:
    def __init__(self, name, age, roll_number):
        self.__name = name  # private attribute
        self.__age = age  # private attribute
        self.__roll_number = roll_number  # private attribute
 
    def get_name(self):
        return self.__name
 
    def set_name(self, name):
        self.__name = name
 
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age.")

    def get_roll_number(self):
        return self.__roll_number

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    def display_details(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Roll Number: {self.__roll_number}")

student1 = Student("Alice", 20, "A123")
student1.display_details()

student1.set_age(21)   
student1.display_details()
