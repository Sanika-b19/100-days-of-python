# Exercise 2: Overload the "/" Operator

from fractions import Fraction

class RationalNumber:
    def __init__(self, numerator, denominator):
        self.fraction = Fraction(numerator, denominator)

    def __truediv__(self, other):
        return self.fraction / other.fraction

    def __str__(self):
        return str(self.fraction)

frac1 = RationalNumber(1, 2)
frac2 = RationalNumber(3, 4)

result = frac1 / frac2
print(f"{frac1} / {frac2} = {result}")
