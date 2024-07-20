# Project for Day 5: Random Password Generator
# This project demonstrates the use of lists, loops, user input, and the random module in Python which i've learnt till now.

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']

user_input_letter = int(input("Enter how many letters you want in your password: "))
user_input_number = int(input("Enter how many numbers you want in your password: "))
user_input_symbol = int(input("Enter how many symbols you want in your password: "))

password = []

# Adding random letters to the password list
for char in range(1, user_input_letter + 1):
    password.append(random.choice(letters))

# Adding random numbers to the password list
for char in range(1, user_input_number + 1):
    password.append(random.choice(numbers))

# Adding random symbols to the password list
for char in range(1, user_input_symbol + 1):
    password.append(random.choice(symbols))

# Shuffling the final password list 
random.shuffle(password)

str_password = ""
for i in password:
    str_password += i

print(str_password)


