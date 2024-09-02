# Exercise 4: Overload the " [] " Operator

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients  

    def __getitem__(self, index):
        return self.coefficients[index]

    def __setitem__(self, index, value):
        self.coefficients[index] = value

    def __str__(self):
        return " + ".join(f"{coef}*x^{i}" for i, coef in enumerate(self.coefficients))

poly = Polynomial([3, 2, 5])  

print(f"Polynomial: {poly}")
print(f"Coefficient of x^2: {poly[2]}")

poly[2] = 6 
print(f"Updated Polynomial: {poly}")
