# Exercise 4: Adding and Subtracting Time

from datetime import datetime, timedelta

current_datetime = datetime.now()

new_datetime_add = current_datetime + timedelta(days=5)

# Subtract 2 hours
new_datetime_subtract = current_datetime - timedelta(hours=2)

print(f"Current date and time: {current_datetime}")
print(f"Date and time after adding 5 days: {new_datetime_add}")
print(f"Date and time after subtracting 2 hours: {new_datetime_subtract}")
