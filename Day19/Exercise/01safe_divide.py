# Exercise 1: Safe Division

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

result = safe_divide(10, 0)
print(result)  
