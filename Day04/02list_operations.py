# Understanding list offset (indexing) and appending items to a list in Python.

# list of fruits
fruits = ['apple', 'banana', 'cherry']

# Accessing elements using offset (indexing)
first_fruit = fruits[0]  # First element
second_fruit = fruits[1]  # Second element
last_fruit = fruits[-1]  # Last element

print(f"First fruit: {first_fruit}")
print(f"Second fruit: {second_fruit}")
print(f"Last fruit: {last_fruit}")

# Appending new items to the list
fruits.append('date')
fruits.append('elderberry')

print(f"List after appending new items: {fruits}")

# Accessing elements after appending
new_last_fruit = fruits[-1]
new_second_last_fruit = fruits[-2]

# Printing accessed elements after appending
print(f"New last fruit: {new_last_fruit}")
print(f"New second last fruit: {new_second_last_fruit}")
