import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
lives = 6

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
    
    
    if guess_letter in display:
        print(f"\nYou have already guessed {guess_letter}")
    
    #Checked Guessed Letter
    for letter in chosen_word:
        if letter == guess_letter:
            display[i] = guess_letter
        i += 1
    print(f"\n{' '.join(display)}") 
    if guess_letter not in chosen_word:
        print(f"\nYou guessed {guess_letter}, that's not in the word. You lose a life.")
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You Lose :(")
            break
        lives -=1
    


    if "_" not in display:
        if lives > 0:
            print("!! YOU WIN !!")
