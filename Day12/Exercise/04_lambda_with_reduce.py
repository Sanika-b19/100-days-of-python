# Exercise 4: Using Lambda with Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Lambda function to find the product of all numbers
product = reduce(lambda x, y: x * y, numbers)

print(f"Product of all numbers: {product}")
