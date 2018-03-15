# step1 
def my_function(input_var1, input_var2):
    print(input_var1,input_var2)
    return input_var1 + input_var2

first_call = my_function(1, 1)
print(first_call)

second_call = my_function(2, 123)
print(second_call)


#step2
def my_function(var1, var2,var3):
    print('No way, I\'m using this: {}, {}, {}'.format(var1, var2, var3))
    return var1 + var2 + var3

# redefined for 3
third_call = my_function(12, 10, 24)
print(third_call)

#
def first(x):
    return x + 10
print(first)
print(first(8))

# summ all
def sum_all(*numbers):
    print(numbers, type(numbers))
    summ = 0
    for sumt in numbers:
        summ += sumt
    print(summ)
    return summ
sum_all(1,2,3,4)

# **kwargs
# обычная функция
def test(a=1, b=2):
    print(a + b)
test(10)
test(b = 10)
test(a = -2)
# в эту функцию можно передать любое кол-во именованых аргументов
def any_kw(**kwargs):
    print(kwargs, type(kwargs))
any_kw(k=1, some=2, wo=3)




        





