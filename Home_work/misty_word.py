# Program "Misty word"
import random

# create words list

wordList = ['plane', 'golf', 'girl', 'ball', 'table',
            'string', 'neko', 'helicopter', 'gate',
            'python', 'lamp', 'fork', 'bullet', 'gyroscope',
            'timetodier'
            ]

# rnd list item & var init
lastListItem = len(wordList)-1
rndInt = random.randint(0, lastListItem)
getInputValue = None


# print list items values and let user to guess some

print('debug rnd =', wordList[rndInt])


def printWL():

    halfwl = 1 + len(wordList) // 2
    n = 1
    i = 0
    max_item_len = 0

    for l in wordList:
        if max_item_len < len(l):
            max_item_len = len(l)

    while i < (halfwl):
        try:
            s_item = wordList[(halfwl + i)]
            f_item = wordList[i]
        except:
            s_item = None
            print('{}: {}'.format(n, wordList[i]))
        if s_item != None:
            var_x = max_item_len - len(f_item)
            tabs = ' ' * var_x
            print('{}: {} {} {}: {}'.format(n, f_item, tabs, halfwl + n, s_item))
        n += 1
        i += 1

    # halfwl = 1 + len(wordList) // 2
    # n = 1
    # i = 0
    # while i < (halfwl):
    #     try:
    #         s_item = wordList[(halfwl + i)]
    #         f_item = wordList[i]
    #     except:
    #         s_item = None
    #         print('{}: {}'.format(n, wordList[i]))
    #     if s_item != None:
    #         if len(f_item) > 8:
    #             tabs = ' \t \t'
    #         else:
    #             tabs = ' \t \t \t'
    #         print('{}: {} {} {}: {}'.format(n,f_item, tabs, halfwl + n, s_item))
    #     n += 1
    #     i += 1
    # pattern = None
    # b = 1
    # print('Misty word is ?')
    # for item in wordList:
    #     if item == wordList[lastListItem]:
    #         print(b, item)
    #     if b % 2 != 0:
    #         pattern = item
    #     else:
    #         print((b - 1), pattern, ' \t', b, item)
    #     b += 1
# EOF printWL

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
    if rndInt != getInputValue:
        print('wrong try more!\n============================')
    else:
        print('Winner! misty word is', wordList[rndInt])

# printWL into columns


