# Exercise 3: Overload the "+=" Operator

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

   def __iadd__(self, other):
        self.real += other.real
        self.imag += other.imag
        return self

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print(f"Before: {c1}")
c1 += c2
print(f"After: {c1}")
