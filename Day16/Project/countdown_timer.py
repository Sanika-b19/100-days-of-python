# Project: Countdown Timer

import time

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds > 0:
        
        hrs = total_seconds // 3600
        mins = (total_seconds % 3600) // 60
        secs = total_seconds % 60

        print(f"{hrs:02d}:{mins:02d}:{secs:02d}", end="\r")
        
         time.sleep(1)
        
        total_seconds -= 1

    print("Time's up!")
 
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Start the countdown
countdown_timer(hours, minutes, seconds)
