# Program "misty int"
# Comp withdraw 1 of 10 misty ints
# You trying to guess until you made right choice
# Program print how many tries you`ve done

import random

rndMistyValue = random.randint(1, 10)
print('I`ve chosen an Rnd_Value! Try to guess')
guessValue = 0
guessNum = 0

while rndMistyValue != guessValue :
    guessValue = int(input("Try to guess which misty value ? = "))
    guessNum += 1

print('Ho ho! You won with {} tries !'.format(guessNum))
