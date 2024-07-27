# Exercise 5: Combining Map, Filter, and Reduce

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Square the numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Step 2: Filter out even numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, squared_numbers))

# Step 3: Find the sum of the remaining numbers
sum_of_odd_numbers = reduce(lambda x, y: x + y, odd_numbers)

print(f"Sum of squared odd numbers: {sum_of_odd_numbers}")
