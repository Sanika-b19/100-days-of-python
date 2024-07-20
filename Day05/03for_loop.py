# For loop in Python.

example_list = [1, 2, 3, 4, 5]
print("For Loop with Lists:")
for item in example_list:
    print(f"Item: {item}")

# Exercise : Finding the maximum item
max_item = example_list[0]
for item in example_list:
    if item > max_item:
        max_item = item
print(f"Maximum item: {max_item}")
