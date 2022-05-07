#Seth Foster
#This script shuffles the wordlist so the output is random and does not repeat words printed.

import random

wordlist = ["Hello", "how", "are", "you"]

#Shuffles the wordlist and then prints the result.
random.shuffle(wordlist)

for item in wordlist:
    print(item)