import random

# Generating a random integer between 1 and 10
random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")

# Generating a random floating-point number between 0 and 1
random_float = random.random()
print(f"Random floating-point number between 0 and 1: {random_float}")

# Generating a random floating-point number between 1 and 10
random_uniform = random.uniform(1, 10)
print(f"Random floating-point number between 1 and 10: {random_uniform}")

# Selecting a random element from a list
choices = ['apple', 'banana', 'cherry', 'date']
random_choice = random.choice(choices)
print(f"Random choice from the list: {random_choice}")

# Shuffling a list
random.shuffle(choices)
print(f"Shuffled list: {choices}")

# Generating a random sample of 2 elements from the list
random_sample = random.sample(choices, 2)
print(f"Random sample of 2 elements from the list: {random_sample}")