# Exercise :  Using Global Variables Across Multiple Functions

# Global variable
total = 0

def add_to_total(amount):
    global total
    total += amount
    print(f"Total after adding: {total}")

def subtract_from_total(amount):
    global total
    total -= amount
    print(f"Total after subtracting: {total}")

add_to_total(10)
subtract_from_total(5)
