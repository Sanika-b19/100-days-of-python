# Exercise 2: Writing to a File

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

write_to_file('output.txt', 'Hello, World!')
