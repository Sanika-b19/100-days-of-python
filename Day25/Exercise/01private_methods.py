# Exercise 1: Implement Private Methods

class MyClass:
    def __init__(self, value):
        self.__value = value  # Private attribute

    def __private_method(self):
        print(f"Private method accessed with value: {self.__value}")

    def access_private_method(self):
        self.__private_method()  # Accessing private method from within the class

obj = MyClass(10)
obj.access_private_method()


# obj.__private_method()  # this line will cause error because we cannot access private method directly
