#Step 1 
import random

from word import word_list
from art import logo, stages
from replit import clear

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
word = random.choice(word_list)
print(f"Solution help : {word}")

display = []
len_word = len(word)

for _ in range(len_word):
    display += "_"
print(display)

END_GAME = False

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
while not END_GAME:  
    guess =  input("Guess a letter : ").lower()
    
    clear()

    print(logo)
    for position in range(len_word):
        letter = word[position]
        #print(f"Current position: {position}\n Current letter: {letter}")
        if letter == guess:
            display[position] = letter
   
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    #Join all the elements in the list and turn it into a String.
    if guess not in word:
        lives -= 1
        if lives == 0:
            END_GAME = True
            print("You lose.")	

    print(f"{' '.join(display)}")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    if "_" not in display:
        END_GAME = True
        print("You win")
    
    print(stages[lives])
