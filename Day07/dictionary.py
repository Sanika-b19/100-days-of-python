# Creating a dictionary
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Accessing dictionary values
print("Dictionary values:")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")

# Adding a new key-value pair
person['email'] = 'alice@example.com'
print("\nUpdated dictionary with new key-value pair:")
print(person)

# Modifying an existing value
person['age'] = 31
print("\nDictionary after modifying an existing value:")
print(person)

# Deleting a key-value pair
del person['city']
print("\nDictionary after deleting a key-value pair:")
print(person)

# Iterating through dictionary keys and values
print("\nIterating through dictionary keys and values:")
for key, value in person.items():
    print(f"{key}: {value}")
