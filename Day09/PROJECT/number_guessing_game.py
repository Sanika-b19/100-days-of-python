# Number guessing game

import random

def level(no):
     '''  
    Plays a number guessing game with the specified number of attempts (int).
    '''
     
     attempts =no
     is_continue = True
     while is_continue:
        print(f"You have {attempts} attempts left ")
        attempts-=1
        user_number = int(input("Make a guess :"))

        if user_number>no_to_be_guessed:
            if attempts == 0:
                print(f"You loose No attempts left. The answer was {no_to_be_guessed}")
                is_continue = False 
            else:           
                print("Too High")           
        if user_number<no_to_be_guessed:
            if attempts == 0:
                print(f"You loose No attempts left. The answer was {no_to_be_guessed}")
                is_continue = False 
            else:           
                print("Too Low")               
        if user_number == no_to_be_guessed:
            print(f"You got it! The answer was {no_to_be_guessed}.")
            is_continue = False


print("welcome to the no guessing game ")
print("You have to guess a no between 1 to 100 ")
print("Choose difficulty level Easy or Hard ?")

difficulty = input("-->").lower()

no_to_be_guessed = random.randint(1,100)

if difficulty == 'easy':
    level(no=10)
else:
    level(no=5)