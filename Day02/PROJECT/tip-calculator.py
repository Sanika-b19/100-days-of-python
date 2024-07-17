# Tip Calculator
# This is my second project for Day 2 of the 100 days of Python coding challenge.
# This program calculates how much each person should pay when splitting a bill, including a tip.

print("Welcome to the Tip Calculator!")
total_bill = int(input("What was the total bill? \n"))
tip = int(input("How much tip would you like to give? \n"))
total_people = int(input("How many people to split the bill? \n"))
payable_amount = float((total_bill + tip) / total_people)

print("Each person should pay:", round(payable_amount, 2))
