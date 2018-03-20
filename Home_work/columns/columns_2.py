# вывод в 2 колонки

word_list = ['plane', 'golf', 'girl', 'ball', 'table',
            'string', 'neko', 'helicopter', 'gate',
            'python', 'lamp', 'fork', 'bullet', 'gyroscope',
            'timetodier', 'Word1', 'Word2'
             ]

half_list_len = 1 + len(word_list) // 2
first_word_number = 1
iteration_counter = 0
max_item_len = 0

for item in word_list:
    if max_item_len < len(item):
        max_item_len = len(item)

while iteration_counter < (half_list_len):
    try:
        second_column_item = word_list[(half_list_len + iteration_counter)]
        first_column_item = word_list[iteration_counter]
    except:
        second_column_item = None
        print('{}: {}'.format(first_word_number, word_list[iteration_counter]))
    if second_column_item != None:
        space_multiplier = max_item_len - len(first_column_item)
        tabs = ' ' * space_multiplier
        print('{}: {} {} {}: {}'.format(first_word_number, first_column_item, tabs, half_list_len + first_word_number, second_column_item))
    first_word_number += 1
    iteration_counter += 1

