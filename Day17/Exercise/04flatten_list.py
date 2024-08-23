# Exercise 4: Flatten a List of Lists

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in list_of_lists for item in sublist]
print(flattened)
