# Exercise :  Nested Functions and Variable Scope

def outer_function():
    outer_var = 'outer'

    def inner_function():
        inner_var = 'inner'
        print(f"Inner variable: {inner_var}")
        print(f"Outer variable accessed from inner function: {outer_var}")

    inner_function()
    # inner_var is not accessible here
    try:
        print(inner_var)
    except NameError as e:
        print(f"Error: {e}")

outer_function()
