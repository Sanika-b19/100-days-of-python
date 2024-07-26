# Exercise : Demonstrating Lifetime of Variables

def variable_lifetime():
    y = 20  # Local variable
    print(f"Local y inside function: {y}")

variable_lifetime()

print(y)  # This will raise an error because y is not defined outside the function
