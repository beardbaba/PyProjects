#Step 4

import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for n in range(len(chosen_word)):
    display.append("_")
# print(display)

while "_" in display:   
    guess_letter = input("\nGuess a letter: ").lower()
    i = 0
    
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess_letter in display:
        print(f"\nYou have already guessed {guess_letter}")
    #Check guessed letter
    for letter in chosen_word:
        if letter == guess_letter:
            display[i] = guess_letter
        i += 1
    print(f"\n{' '.join(display)}") 
    if guess_letter not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"\nYou guessed {guess_letter}, that's not in the word. You lose a life.")
        # print(f"{' '.join(display)}")
        #TODO-2: - Import the stages from hangman_art.py and make this error go away.
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You Lose :(")
            break
        lives -=1
    

    #Join all the elements in the list and turn it into a String.
    if "_" not in display:
        if lives > 0:
            print("!! YOU WIN !!")
