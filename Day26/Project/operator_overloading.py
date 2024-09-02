# Project: Overload Operators for Custom Classes

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overloading the '+' operator
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    # Overloading the '-' operator
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    # Overloading the '*' operator
    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

    
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

   def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print(f"c1: {c1}")
print(f"c2: {c2}")

c3 = c1 + c2
print(f"c1 + c2 = {c3}")

c4 = c1 - c2
print(f"c1 - c2 = {c4}")

c5 = c1 * c2
print(f"c1 * c2 = {c5}")

print(f"c1 == c2: {c1 == c2}")
