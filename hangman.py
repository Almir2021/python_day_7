# Step 1
import random



import hangman_art
hangman_art.stages 

import hangman_words 
word_list = hangman_words.word_list

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
guessing_word = []
lifes = 6
dispaly = 0
already_guessed = []
lenght_of_word = len(chosen_word)
chosen_list = list(chosen_word)
print(hangman_art.logo)
for l in range(lenght_of_word):
    print("_ ", end="")
print()
for l in range(lenght_of_word):
    guessing_word.append(" ")
    # print(chosen_list[l])
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

while lifes != 0:
        guess = str(input("Take a guess  "))
        guess = guess.lower()
        print(guess)
    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        if guess in guessing_word:
           print(f" Letter {guess} you already guessed")

        if guess in chosen_word:
           for l in range(lenght_of_word):
            # print(chosen_list[l])
             if guess == chosen_list[l]:
                guessing_word.pop(l)
                guessing_word.insert(l, guess)
                 
                
        else:
              lifes -= 1
              if lifes <=5  :
                 #print(stages[lifes]) 
                 dispaly =1
        if dispaly ==1:
         print(hangman_art.stages[lifes])      
        print(guessing_word)

        if all([char in guessing_word for char in chosen_list]):
         print("You won") 
         break
        
        if lifes == 0:
            print("You lost")
            print(f"the word to guess was {chosen_word} ")


