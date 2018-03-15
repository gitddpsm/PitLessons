# Recursion:
# import traceback


def factorial(n): # This function is recusive it calls itself
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) # 4 * 3 * 2 * 1 = 24



def print_all_list_items(data):
    if not data:
        return
    item = data.pop()
    print(item)
    return print_all_list_items(data)


print_all_list_items(['1', '2', 'end'])
