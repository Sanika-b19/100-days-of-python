# working with nested lists in Python.

fruits = ['apple', 'banana', 'cherry']

# Correctly accessing elements within the list bounds
print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")
print(f"Third fruit: {fruits[2]}")

# nested list
nested_list = [
    ['apple', 'banana', 'cherry'],
    ['date', 'elderberry', 'fig'],
    ['grape', 'honeydew', 'kiwi']
]

# Accessing elements 
first_inner_list = nested_list[0]
second_inner_list = nested_list[1]
third_inner_list = nested_list[2]

# Accessing elements directly
first_element_first_list = nested_list[0][0]
second_element_first_list = nested_list[0][1]
third_element_first_list = nested_list[0][2]

first_element_second_list = nested_list[1][0]
second_element_second_list = nested_list[1][1]
third_element_second_list = nested_list[1][2]

first_element_third_list = nested_list[2][0]
second_element_third_list = nested_list[2][1]
third_element_third_list = nested_list[2][2]

# Printing accessed elements
print(f"First inner list: {first_inner_list}")
print(f"First element of the first inner list: {first_element_first_list}")
print(f"Second element of the first inner list: {second_element_first_list}")
print(f"Third element of the first inner list: {third_element_first_list}")

print(f"Second inner list: {second_inner_list}")
print(f"First element of the second inner list: {first_element_second_list}")
print(f"Second element of the second inner list: {second_element_second_list}")
print(f"Third element of the second inner list: {third_element_second_list}")

print(f"Third inner list: {third_inner_list}")
print(f"First element of the third inner list: {first_element_third_list}")
print(f"Second element of the third inner list: {second_element_third_list}")
print(f"Third element of the third inner list: {third_element_third_list}")
