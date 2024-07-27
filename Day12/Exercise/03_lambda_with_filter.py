# Exercise 3: Using Lambda with Filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lambda function to filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Even numbers: {even_numbers}")
