# Exercise 5: Parsing Dates from Strings

from datetime import datetime

date_str1 = "2024-07-16"
date_str2 = "July 16, 2024"
date_str3 = "16/07/2024 14:30"

# Parse the date strings
parsed_date1 = datetime.strptime(date_str1, "%Y-%m-%d")
parsed_date2 = datetime.strptime(date_str2, "%B %d, %Y")
parsed_date3 = datetime.strptime(date_str3, "%d/%m/%Y %H:%M")

print(f"Parsed date 1: {parsed_date1}")
print(f"Parsed date 2: {parsed_date2}")
print(f"Parsed date 3: {parsed_date3}")
