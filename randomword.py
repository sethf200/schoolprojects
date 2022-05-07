#Random Word Game.
#Picks a random word and lets the user guess.
#Seth Foster

import random
import string
#My wordlist.
WORDS = ("random", "python", "snake", "pottery", "code", "have", "not", "country")

word = random.choice(WORDS)

print("Welcome to Random Word Game!")
print("\nYou get 5 guesses!")


guess = input("Guess the word: ")
tries = 1

while guess != word and tries !=5:
    if guess == word:
        print("Congrats! You got it!")
    else:
        print("Sorry, wrong answer.")
    guess = input("\nGuess the word: ")
    tries += 1

if tries == 5:
    print("\nSorry! You didn't get it in time!")
    print("The word was: " + word + ".")
else:
    print("You guessed it right! Congratulations!")
    print("\nIt only took you", tries, "tries!")