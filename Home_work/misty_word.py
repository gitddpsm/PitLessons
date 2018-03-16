# Program "Misty word"
import random

# create words list

wordList = ('plane', 'golf', 'girl', 'ball', 'table', 'string', 'neko', 'helicopter', 'gate', 'python')

# rnd list item

rndInt = random.randint(0,9)

# print list items values and let user to guess some
# print('deug rnd =',wordList[rndInt])

def printWL():
    b = 0
    print('Misty word is ?')
    for item in wordList:
        print(b, item)
        b += 1

printWL()

while rndInt != int(input('enter guess num: ')):
    print('wrong try more!\n==========================================')
    printWL()
else:
    print('Gotcha! Misty word is ', wordList[rndInt])