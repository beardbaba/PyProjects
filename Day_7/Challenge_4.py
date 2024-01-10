#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for n in range(len(chosen_word)):
    display.append("_")
print(display)

while "_" in display:   
    guess_letter = input("Guess a letter: ").lower()
    i = 0

#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Check guessed letter
    for letter in chosen_word:
        if letter == guess_letter:
            display[i] = guess_letter
        i += 1
    if guess_letter not in chosen_word:
        print(stages[lives])
        lives -=1
        if lives < 0:
            print("You Lose :(")
            break
    print(f"{''.join(display)}") 

    #Join all the elements in the list and turn it into a String.
if "_" not in display:
    if lives > 0:
        print("!! YOU WIN !!")
