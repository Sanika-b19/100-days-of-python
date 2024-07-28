# Exercise 3: Countdown Timer with Alarm Sound

import time
import winsound

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
    winsound.Beep(440, 1000)  

countdown_time = int(input("Enter the time in seconds: "))
countdown(countdown_time)
