# Exercise 4: Input Validation with Retry Mechanism

def get_integer():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

number = get_integer()
print(f"You entered: {number}")
