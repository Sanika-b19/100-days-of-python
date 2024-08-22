# Exercise 4: Format Date and Time

from datetime import datetime
 
now = datetime.now()

format1 = now.strftime("%d/%m/%Y")
format2 = now.strftime("%m-%d-%Y %H:%M:%S")
format3 = now.strftime("%A, %d %B %Y")

print("Format 1:", format1)
print("Format 2:", format2)
print("Format 3:", format3)
