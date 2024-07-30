# Exercise 3: Appending to a File

def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

append_to_file('output.txt', '\nHello, again!')
