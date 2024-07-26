# Exercise : Global vs Local Variables

# Global variable
x = 10

def global_vs_local():
    # Local variable
    x = 5
    print(f"Local x inside function: {x}")

global_vs_local()
print(f"Global x outside function: {x}")
