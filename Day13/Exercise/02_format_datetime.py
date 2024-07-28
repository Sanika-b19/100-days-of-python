# Exercise 2: Formatting Dates and Times

from datetime import datetime

current_datetime = datetime.now()

# Format the date and time
formatted_date = current_datetime.strftime("%Y-%m-%d")
formatted_time = current_datetime.strftime("%H:%M:%S")
formatted_datetime = current_datetime.strftime("%A, %B %d, %Y %I:%M %p")

print(f"Formatted date: {formatted_date}")
print(f"Formatted time: {formatted_time}")
print(f"Formatted date and time: {formatted_datetime}")
