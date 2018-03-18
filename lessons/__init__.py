print('Help me!')
x = ord('a') # char num
y = x + 2
print('={}={}='.format(x, y))
l = [1, 2]
t = (1, 2)
print(type(l), type(t))

def getInput():
    outVal = None
    while outVal == None:
        try:
            outVal = (int(input('enter guess num: ')) - 1)
            print(outVal)
        except ValueError as e:
            print('please enter int')

getInput()

print('4' * 4)