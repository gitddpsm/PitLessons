# ('Функция выбрасывает исключения')

import random # генератор импортируем

# 1 одно из трех исключений рандомно, ValueError, TypeError, RuntimeError
# в месте вызова обработать все 3 исключения
# 

rndval = random.randint(1,3)
print('Rnd =',rndval)

def throwRndEcxeption():
    err_types = {1:ValueError, 2:TypeError, 3:RuntimeError}
    raise err_types[random.randint(1,3)]

try:
    throwRndEcxeption()
except ValueError:
    print('catch ValueError')
except TypeError:
    print('catch TypeError')
except RuntimeError:
    print('catch RuntimeError')

# 2 Написать функцию принимающую на вход список, 
# если в списке все объекты - int, сортируем список
# иначе ValueError

def intChekSrt(varsIn):
    all_Int = True
    for elem in varsIn:
        if not isinstance(elem, int):
            all_Int = False
    if all_Int:
        varsIn.sort()
        return varsIn
    else:
        raise ValueError

print(intChekSrt([1,5,3,6,8,2,4,7,9]))

# 3 Написать функцию, которая принимает словарь, преобразует ключи словаря к строкам 
# и возвращает новый словарь 

def transform(dict1):
    print('=== transform ===')
    print(type(dict1))
    tsf = dict()
    for key,value in dict1.items():
        tsf[str(key)] = value
    return tsf

print(transform({1:23,2:56,3:1,4:40}))

 
# 4 написать функцию которая принимает писок чисел и возвращает их произведение

def intMultiply(*numbers):
    print('=== intMultipy ===')
    funcVal = 1
    print('get int`s',numbers)
    for i in numbers:
        print('умножаем',funcVal,'на', i)
        funcVal *= i
    return funcVal

print('returned from intMultiply',intMultiply(8,2,3))

    


