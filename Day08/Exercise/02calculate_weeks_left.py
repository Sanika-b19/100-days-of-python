# Calculate the number of weeks left until age 90

current_age = int(input("Enter your current age: "))

#target age
target_age = 90

# number of years left
years_left = target_age - current_age

# number of weeks left
weeks_left = years_left * 52

print(f"You have {weeks_left} weeks left.")
