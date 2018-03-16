# Program misty int
# Comp withdraw 1 of 10 misty ints
# You trying to guess until you made right choise
# Program print how many tryes you`ve done

import random

rndMistyValue = random.randint(1, 10)
print('Rnd value =', rndMistyValue)

guessValue = input("Try to guess which misty value ?")
print(guessValue)
