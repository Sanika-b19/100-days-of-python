# Exercise 1: Debugging with Print Statements

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        print(f"Comparing {num} with {max_num}")  # Debug print
        if num > max_num:
            max_num = num
            print(f"New max found: {max_num}")  # Debug print
    return max_num

numbers = [3, 5, 2, 8, 6]
max_number = find_max(numbers)
print(f"The maximum number is: {max_number}")
