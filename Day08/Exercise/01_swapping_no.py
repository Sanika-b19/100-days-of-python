# Exercise: Swapping Two Numbers

# Function to swap two numbers
def swap(a, b):
    a, b = b, a
    return a, b


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# before swapping
print(f"Before swapping: num1 = {num1}, num2 = {num2}")

num1, num2 = swap(num1, num2)

# after swapping
print(f"After swapping: num1 = {num1}, num2 = {num2}")
