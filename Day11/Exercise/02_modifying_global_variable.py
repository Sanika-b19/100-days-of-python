# Exercise : Modifying Global Variables

# Global variable
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

increment()
print(f"Counter outside function: {counter}")
