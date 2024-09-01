# Exercise 2: Read-Only Attributes

class ReadOnlyClass:
    def __init__(self, name):
        self.__name = name  # Private attribute

    # Getter method to read the attribute
    @property
    def name(self):
        return self.__name

obj = ReadOnlyClass("Alice")
print(obj.name)


# obj.name = "Bob" # this is read-only attribute so it will cause an error
