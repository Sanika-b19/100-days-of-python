# Exercise 3: Days Until Next Birthday

from datetime import datetime, timedelta
 
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

 
today = datetime.today()
 
next_birthday = datetime(today.year, birthdate.month, birthdate.day)
 
if next_birthday < today:
    next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)

 
days_until_birthday = (next_birthday - today).days
print(f"Days until your next birthday: {days_until_birthday} days.")
