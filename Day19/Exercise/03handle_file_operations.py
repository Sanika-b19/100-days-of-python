# Exercise 3: Handling File Operations

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied."

content = read_file("nonexistent_file.txt")
print(content)
