# Exercise 3: Create a Dictionary from Two Lists

keys = ['name', 'age', 'city']
values = ['Alice', 28, 'New York']
my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)
