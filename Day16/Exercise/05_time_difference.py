# Exercise 5: Time Difference Calculator

from datetime import datetime
 
timestamp1 = input("Enter the first timestamp (YYYY-MM-DD HH:MM:SS): ")
timestamp2 = input("Enter the second timestamp (YYYY-MM-DD HH:MM:SS): ")
 
time1 = datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S")
time2 = datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S")

 time_difference = time2 - time1

 days = time_difference.days
seconds = time_difference.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"Time difference: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
