# Defining a function
def greet(name):

    print(f"Hello, {name}!")

# Calling the function
greet("Alice")
greet("Bob")

# Function with return value
def add(a, b):
    """
    Function to add two numbers and return the result.
    Args:
    a (int): First number.
    b (int): Second number.
    Returns:
    int: Sum of a and b.
    """
    return a + b

# Calling the function and printing the result
result = add(5, 3)
print(f"The sum is: {result}")
