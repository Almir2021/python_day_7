# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
guessing_word = []
lifes = 0
lenght_of_word = len(chosen_word)
chosen_list = list(chosen_word)
for l in range(lenght_of_word):
    print("_ ", end="")
print()
for l in range(lenght_of_word):
    guessing_word.append(" ")
    # print(chosen_list[l])
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
if lifes <= 7:
    for i in range(7):
        guess = str(input("Take a guess  "))
        guess = guess.lower()
        print(guess)
    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        for l in range(lenght_of_word):
            # print(chosen_list[l])
            if guess == chosen_list[l]:
                guessing_word.pop(l)
                guessing_word.insert(l, guess)
            else:
                lifes += 1

        print(guessing_word)
else:
    print("You lost")

print(lifes)
