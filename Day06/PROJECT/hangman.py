
import random


word_list = [ "red", "blue", "green", "yellow", "purple", "orange", "pink", "black", "white",
        "brown", "gray", "cyan", "magenta", "maroon", "navy", "olive", "teal", "violet",
        "indigo", "gold", "silver"]

# Hangman stages represented as ASCII art
stages = ['''
   +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
 '''
   +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', 
'''
   +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
 '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


random_choice = random.choice(word_list)

# display list with underscores for each letter in the chosen word
display = []
for every_letter in random_choice:
    display += "_"

# number of lives
lives = 6
length = len(random_choice)
end_of_game = False
guessed_again = 0

# Main game loop
while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
            print(f"You've already guessed {guess}")
    
    # Check if the guessed letter is in the chosen word
    for pos in range(length):
        letter = random_choice[pos]
        if letter == guess:
            guessed_again+=1
            display[pos] = letter
    
    
    # If the guessed letter is not in the chosen word
    if guess not in random_choice:
        lives -= 1
        print(f"You guessed {guess}, thay's not in the word. You lose a life!")
        # If lives reach 0, the player loses
        if lives == 0:
            end_of_game = True
            print("You lose")
    
   
    print(' '.join(display))

    # If there are no more underscores, the player wins
    if "_" not in display:
        end_of_game = True
        print("You won!")

    print(stages[lives])
