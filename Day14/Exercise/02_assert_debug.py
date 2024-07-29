# Exercise 2: Debugging with Assertions

def calculate_average(numbers):
    assert len(numbers) > 0, "List of numbers must not be empty"
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [10, 20, 30, 40]
average = calculate_average(numbers)
print(f"The average is: {average}")
