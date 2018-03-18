# вывод в 2 колонки

wordList = ['plane', 'golf', 'girl', 'ball', 'table',
            'string', 'neko', 'helicopter', 'gate',
            'python', 'lamp', 'fork', 'bullet', 'gyroscope',
            'timetodier', 'Word1', 'Word2'
            ]

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

