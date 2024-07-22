# Nesting dictionaries inside lists in Python.

# Creating a list of dictionaries
students = [
    {'name': 'Alice', 'age': 21, 'major': 'Physics'},
    {'name': 'Bob', 'age': 22, 'major': 'Mathematics'},
    {'name': 'Charlie', 'age': 20, 'major': 'Biology'}
]

# Accessing dictionaries in a list
print("Accessing dictionaries in a list:")
print(f"First student's name: {students[0]['name']}")
print(f"Second student's age: {students[1]['age']}")

# Adding a new dictionary to the list
new_student = {'name': 'Diana', 'age': 23, 'major': 'Chemistry'}
students.append(new_student)
print("\nList after adding a new dictionary:")
print(students)

# Modifying a dictionary in the list
students[0]['age'] = 22
print("\nList after modifying a dictionary:")
print(students)

# Iterating through a list of dictionaries
print("\nIterating through a list of dictionaries:")
for student in students:
    print(f"{student['name']} is {student['age']} years old and majors in {student['major']}.")
