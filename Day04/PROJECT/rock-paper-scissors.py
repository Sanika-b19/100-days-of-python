# Rock, Paper, Scissors
# This is my Project for the day 4 in 100 days of python challenge

import random

#rock
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

#paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''

#scissor
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
print("Welcome to the Rck Paper Scissors Game")
print("Enter 0 for 'ROCK', 1 for the 'PAPER' and 2 for the 'SCISSOR' ")
user = int(input("-->"))
game_image = [rock,paper,scissor]

computer = random.randint(0,2)


if user == 0 and computer == 1:
    print("You chose : ")
    print(game_image[user])
    print("Computer chose :  ")
    print(game_image[computer])
    print("You loose")
elif user == 1 and computer == 2:
        print("You chose : ")
        print(game_image[user])
        print("Computer chose :")
        print(game_image[computer])
        print("You loose")
elif user == 2 and computer == 1:
        print("You chose : ")
        print(game_image[user])
        print("Computer chose :")
        print(game_image[computer])
        print("You Win")
elif user ==0 and computer==2:
        print("You chose :")
        print(game_image[user])
        print("Computer chose :")
        print(game_image[computer])
        print("You Win")
elif user==2 and computer==0:
        print("You chose : ")
        print(game_image[user])
        print("Computer chose :")
        print(game_image[computer])
        print("You loose")
elif user ==1 and computer==0:
        print("You chose : ")
        print(game_image[user])
        print("Computer chose :") 
        print(game_image[computer])
        print("you Win!")
elif user == computer:
        print("You chose : ")
        print(game_image[user])
        print("Computer chose :")
        print(game_image[computer])
        print("It's a Draw")
else :
    print("Enter Valid Number")
    