# вывод в 2 колонки

wordList = ['plane', 'golf', 'girl', 'ball', 'table',
            'string', 'neko', 'helicopter', 'gate',
            'python', 'lamp', 'fork', 'bullet', 'gyroscope',
            'timetodier', 'Word1', 'Word2'
            ]

halfwl = 1 + len(wordList) // 2
n = 1
i = 0
while i < (halfwl):
    try:
        s_item = wordList[(halfwl + i)]
        f_item = wordList[i]
    except:
        s_item = None
        print('{}: {}'.format(n, wordList[i]))
    if s_item != None:
        if len(f_item) > 8:
            tabs = ' \t \t'
        else:
            tabs = ' \t \t \t'
        print('{}: {} {} {}: {}'.format(n,f_item, tabs, halfwl + n, s_item))
    n += 1
    i += 1

