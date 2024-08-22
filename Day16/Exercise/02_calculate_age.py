# Exercise 2: Calculate Age

from datetime import datetime

 
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

today = datetime.today()

years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

if days < 0:
    months -= 1
    days += (today - datetime(today.year, today.month - 1, birthdate.day)).days

if months < 0:
    years -= 1
    months += 12

print(f"Your age is {years} years, {months} months, and {days} days.")
