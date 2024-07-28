# Exercise 3: Calculating the Difference Between Two Dates

from datetime import datetime

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 7, 16)

# Calculate the difference
difference = date2 - date1

print(f"Difference between {date2.date()} and {date1.date()} is {difference.days} days")
