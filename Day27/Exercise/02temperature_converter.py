# Exercise 2: Convert Temperatures Using Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

print(TemperatureConverter.celsius_to_fahrenheit(25))  # Output: 77.0
print(TemperatureConverter.fahrenheit_to_celsius(77))  # Output: 25.0
