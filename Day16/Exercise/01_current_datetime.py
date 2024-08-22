# Exercise 1: Get Current Date and Time
from datetime import datetime

# Get current date and time
now = datetime.now()

current_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", current_time)
