# Nesting lists inside dictionaries in Python.

# Creating a dictionary with lists as values
courses = {
    'math': ['algebra', 'geometry', 'calculus'],
    'science': ['biology', 'chemistry', 'physics']
}

# Accessing lists in a dictionary
print("Accessing lists in a dictionary:")
print(f"Math courses: {courses['math']}")
print(f"First science course: {courses['science'][0]}")

# Adding a new item to a list in the dictionary
courses['math'].append('statistics')
print("\nDictionary after adding a new item to a list:")
print(courses)

# Modifying an item in a list in the dictionary
courses['science'][1] = 'earth science'
print("\nDictionary after modifying an item in a list:")
print(courses)

# Iterating through lists in a dictionary
print("\nIterating through lists in a dictionary:")
for subject in courses:
    print(f"{subject.capitalize()} courses:")
    for course in courses[subject]:
        print(f"{course}")
