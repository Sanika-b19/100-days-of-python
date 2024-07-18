# Project Title: Treasure Hunt Game
# This is my third day project.
#A simple text-based adventure game where the player makes choices to find a treasure.

#Made use of ASCII Art
print('''  
  _______                                  _    _             _   
 |__   __|                                | |  | |           | |  
    | |_ __ ___  __ _ ___ _   _ _ __ ___  | |__| |_   _ _ __ | |_ 
    | | '__/ _ \/ _` / __| | | | '__/ _ \ |  __  | | | | '_ \| __|
    | | | |  __| (_| \__ | |_| | | |  __/ | |  | | |_| | | | | |_ 
    |_|_|  \___|\__,_|___/\__,_|_|  \___| |_|  |_|\__,_|_| |_|\__|                                                                                                                                                           
''')

print("Welcome to the TREASURE HUNT")
print("Get ready to explore exciting adventure")
print("Solve mysterious puzzles to overcome challenges to find treasure")
print("Are you ready ? [Type Yes/No to continue]")
start = input("-->")
if start!='Yes' or start!='yes' or start!='No' or start!='no':
   print("Type Yes Or No!")   
if start == 'Yes' or start=='yes':
    print("There is a one choice you can choose a way Right or Left, be careful and make a choice")
    choice1 = input("-->")
    if choice1 == 'Left' or choice1 == 'left':
        print("You've moved one step forword towards your treasure and you have a puzzle to solve")
        print("complete the series [ 2,4,8,16,? ] ")
        choice2 = input("-->")
        if choice2=='32':
          print("Congratulation That's right !!\nYou are just one step away from getting your treasure\nTo move forward select a door")
          print("Red, Yellow, Blue choose wisely!!")
          choice3 = input("-->")
          if choice3 == 'Yellow' or choice3=='yellow':
            
            #ASCII Art
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')
            print("Hurray !! Congratuations You found the treasure!!")
          elif choice3=='Red' or choice3=='red':
            print("It's a room full of fire. Game Over! ")
          elif choice3=='Blue' or choice3=='blue':
            print("You entered a room full of beast. Game over! ")
          else:
            print("You entered a door that does not exists. Game Over!")
        else:
            print("Wrong Answer. Game Over!!")
          
    else:
      print("Game over you fell into a hole!")        
else:
    print("See you soon !")
    