# Exercise 1: Reading from a File

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

read_file('example.txt')
