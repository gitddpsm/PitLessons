# local scope

def scoped_func(arg):
    value = arg * 10
    print(value)

scoped_func(2)
print()

# Returning something

def return_some(input_value):
    calc = input_value - 7
    print(calc)
    return calc

print(return_some(4))

# Global scope

SOME_VAR = 'value'

def print_var():
    print(SOME_VAR)

print_var()

# You can not modify global scope

def modify_var():
    try:
        SOME_VAR += '_extra'
    except UnboundLocalError as e:
        print('Eerror', e)

modify_var()
print(SOME_VAR)

# But you can mutate it

GLOBAL_LIST = []

def append_to_list(item):
    print('Adding', item)
    GLOBAL_LIST.append(item)

append_to_list(1)
append_to_list(3)
print(GLOBAL_LIST)
