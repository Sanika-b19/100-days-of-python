# Logical AND
age = int(input("Enter your age: "))
has_permit = input("Do you have a driving permit? (yes/no): ").lower() == 'yes'

if age >= 18 and has_permit:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

# Logical OR
has_cash = input("Do you have cash? (yes/no): ").lower() == 'yes'
has_card = input("Do you have a credit/debit card? (yes/no): ").lower() == 'yes'

if has_cash or has_card:
    print("You can make a purchase.")
else:
    print("You cannot make a purchase.")

# Logical NOT
is_raining = input("Is it raining? (yes/no): ").lower() == 'yes'

if not is_raining:
    print("You can go for a walk.")
else:
    print("You might want to stay inside.")
