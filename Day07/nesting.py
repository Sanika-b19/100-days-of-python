nested_dict = {
    'person1': {
        'name': 'Alice',
        'age': 30,
        'hobbies': ['reading', 'hiking']
    },
    'person2': {
        'name': 'Bob',
        'age': 25,
        'hobbies': ['cycling', 'gaming']
    }
}

# Accessing nested dictionary
print("Accessing nested dictionary:")
print(f"Person1's name: {nested_dict['person1']['name']}")
print(f"Person2's hobbies: {nested_dict['person2']['hobbies']}")

# Modifying nested dictionary
nested_dict['person1']['age'] = 31
nested_dict['person2']['hobbies'].append('swimming')

print("\nModified nested dictionary:")
print(nested_dict)

# Nesting List into Dictionary
list_in_dict = {
    'fruits': ['apple', 'banana', 'cherry'],
    'vegetables': ['carrot', 'broccoli', 'spinach']
}

# Accessing list inside a dictionary
print("\nAccessing list inside a dictionary:")
print(f"Fruits: {list_in_dict['fruits']}")
print(f"First vegetable: {list_in_dict['vegetables'][0]}")

# Modifying list inside a dictionary
list_in_dict['fruits'].append('date')
list_in_dict['vegetables'][1] = 'bell pepper'

print("\nModified list inside a dictionary:")
print(list_in_dict)
