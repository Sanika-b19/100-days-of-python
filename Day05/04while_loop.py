# While loop in Python.

print("While Loop:")
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1

# Exercise : Finding factorial of a number
number = 5
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"Factorial of {number}: {factorial}")
