# Program "Misty word"
import random

# create words list

wordList = ['plane', 'golf', 'girl', 'ball', 'table',
            'string', 'neko', 'helicopter', 'gate',
            'python', 'lamp', 'fork', 'bullet', 'gyroscope',
            'timetodier'
            ]

# rnd list item & var init

rndInt = random.randint(0,len(wordList)-1)
getInputValue = None


# print list items values and let user to guess some

print('deug rnd =',wordList[rndInt])


def printWL():
    pattern = None
    b = 1
    print('Misty word is ?')
    for item in wordList:
        if item == wordList[(len(wordList)-1)]:
            print(b, item)
        if b % 2 != 0:
            pattern = item
        else:
            print((b - 1), pattern, ' \t', b, item)
        b += 1


def getInput():
    outVal = None
    while outVal == None:
        try:
            outVal = (int(input('enter guess num: ')) - 1)
            if outVal < 0:
                outVal = None
                raise TypeError
            return outVal
        except ValueError:  # string input exception
            print('Please enter int')
        except TypeError:
            print('Please enter positive int > 0')


while rndInt != getInputValue:
    printWL()
    getInputValue = getInput()
    print('wrong try more!\n============================')

else:
    print('Winner! misty word is', wordList[rndInt])

# printWL into columns


