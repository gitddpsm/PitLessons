print('hello world')
varPrintString = 'nya nya varstring is ok!'

try:
    d = {'key': 23}
    d = (1 / 0) 
    print(d,('des not exist'))
except ZeroDivisionError as err1:
    print("This wont't be called{}",err1)


#try:
#	1 / int(input('x: '))
#except ZeroDivisionError:
#	print('error /0')
#except TypeError:
#	print('TypeError')
#except ValueError:
#	print('Bad input')
#a = int(input('x: '))