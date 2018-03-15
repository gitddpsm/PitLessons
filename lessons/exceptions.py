l = [1,9]
try:
    l[9]
except IndexError as e:
    print('Out f range', e)

#x = int(input('x: ', ))
#x = 23
#print("hello, your errror: {}".format(x))

# Catching speific exception

try:
    print(1/0)
except ZeroDivisionError:
    print("This /0!!!")

try:
    print(1/0)
except ZeroDivisionError as e:
    print("Zeroexception to var")
    print('Error for 1/0 :',e)
# Value Err
try:
    int('ff')
except ValueError as i_knew_it:
    print('Error for int(\'ff\') :',i_knew_it)

# Type Err
try:
    3 / 'asd'
except TypeError as e:
    print('Type error :', e)

#Multiple except blocks
print('============= multiple error ===============')
try:
    raise ValueError()
except ZeroDivisionError:
    print('Divided by zero!')
except AttributeError:
    print('Key is missing')
except Exception as ex:
    print('I don\'t know what\'s going on')
    print(ex)


# try/exept/finally
print('=========== try/except/finally =============')
try:
    print(1 / 0)
except ZeroDivisionError:
    print('0 !! нуль! вы чегно делаити!')
finally:
    print('Это сообщение о конце!')

# try/except/else
print('============= try/except/else ==============')
try:
    print('Fine')
except KeyError:
    print('Nope.')
else:
    print('Else clause')

#All together
print('=============== All together ===============')
try:
    print('Try')
except ValueError:
    pass #you shuld never pass on executions!
else: print('else')
finally:
    print('Finnaly!')