# Exercise 1: Calculate Factorials Using Static Methods

class MathUtils:
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * MathUtils.factorial(n-1)

print(MathUtils.factorial(5))  # Output: 120
