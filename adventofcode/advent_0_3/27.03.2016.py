import json



def init_dict(ffile_in):
    try:
        json_input = open(ffile_in).read() #    откр фл на чтение
        turns_dict = json.loads(json_input) #  модулем json всасываем открытый файл
        print(turns_dict.get('ver'), 'loaded ver') # тестируем словарь,
        ver = turns_dict.get('ver') + 1
        turns_dict = {}
        turns_dict.update({'ver': ver})
        with open(ffile_in, 'w') as ffile: # модулем заливаем словарь в файл
            json.dump(turns_dict, ffile, sort_keys=True, indent=4)
    except:
        turns_dict = {}
        with open(ffile_in, 'w') as ffile:
            turns_dict.update({'ver': 0})
            json.dump(turns_dict, ffile, sort_keys=True, indent=4)
    return turns_dict

def wr_dict():
    with open(ffile_in, 'w') as ffile:
        json.dump(turns_dict, ffile, sort_keys=True, indent=4)

ffile_in = '2703_data_3.0.1.json'
print(init_dict(ffile_in))
turns_dict = init_dict(ffile_in)


elcord = '0_0'
el_x = 0
el_y = 0
el_hist = 0

def get_xy_val(x, y):
    xy = '{}_{}'.format(x, y)
    location = turns_dict.get(xy)
    return {xy: location}

def set_xy_val(x, y, turn_num):
    # xy = '{}_{}'.format(x, y)
    # if xy in turns_dict.keys():
    #     buffer = (turns_dict.get(xy)['vis_hist'], turn_num)
    #     turns_dict.update({xy:{'int_x':x,'int_y':y,'vis_hist':buffer}})
    # else:
    #     turns_dict.update({xy:{'int_x':x,'int_y':y,'vis_hist':turn_num}})
    print('локация с параметрами')
    print(x,y,turn_num, 'в разработке')
    return print('ok')


element = {elcord: {'int_x': el_x, 'int_y': el_y, 'vis_hist': el_hist}}
turns_dict.update(element)


print(turns_dict, 'END')
srtout = turns_dict.get('0_0')
print(get_xy_val(0, 0), '==== get_xy_val(0, 0)')
set_xy_val(1,0,1)
print(turns_dict)
print(turns_dict.get('0_0')['vis_hist'])

turn_num = 77 # path_num
path_num = 77
path_item = [path_num]
xy = '77_77'
x = 77
y = 77

try:
    print('debug ========================== 1')

    # print(turns_dict.get(xy)['vis_hist'], turn_num)
    # oper = (turns_dict.get(xy)['vis_hist'], turn_num)
    # turns_dict.update({xy:{'int_x':x,'int_y':y,'vis_hist':oper}})
    # turns_dict.update({'iuh': 'prinvet'})
    try:
        print('try test _ try in try')
        print(xy , x, y, path_item, path_num, turn_num)
        print(turns_dict.get(xy)['vis_hist'], 'EOF ======1')

    except:
        print('exept in try in try')
    print(xy)
    # print(turns_dict.get(xy)['vis_hist'], 'EOF ======1')

except TypeError:
    print('fuck in your try', turn_num, 'генерируем новую локацию!' )
    set_xy_val(x,y,turn_num)

try:
    print('try test')

except:
    print('exept in try')

try:
    print('debug ========================== 2')
    print(',kjr ytdblfyyjq ibps')
    xy = '{}_{}'.format(x, y)
    if xy in turns_dict.keys():
        buffer = (turns_dict.get(xy)['vis_hist'], turn_num)
        turns_dict.update({xy:{'int_x':x,'int_y':y,'vis_hist':buffer}})
    else:
        turns_dict.update({xy:{'int_x':x,'int_y':y,'vis_hist':turn_num}})
    print(json.dump(turns_dict, sort_keys=True, indent=4))
except:
    print('except in try == 2')

turns_dict = init_dict(ffile_in)
print(init_dict(ffile_in))
print(turns_dict)
set_xy_val(0,0,0)

xy = '{}_{}'.format(x, y)
if xy in turns_dict.keys():
    print('?', xy)
else:
    print(turns_dict.keys())
    print(turns_dict)
    print('---------------------------------')

# def set_xy_val(x, y, turn_num):
print(turns_dict.get('0_0')) # none
print(turns_dict.get('ver')) # int
print(xy,x, y, turn_num)
if turns_dict.get(xy) != None:
    print(' != none', print(xy))
else:
    print('else')
# print('локация с параметрами')
    print(xy,x,y,turn_num, 'в разработке')
# return print('ok')
####################### dict.pop(key[, default])
# - удаляет ключ и возвращает значение.
# Если ключа нет, возвращает default
# (по умолчанию бросает исключение).
print(turns_dict.pop('ver'))
turns_dict = init_dict(ffile_in)
print(turns_dict)
try:
    print(turns_dict.pop('er'))
except:
    print('error Key Error')

get_xy_val(x,y)
print(get_xy_val(x,y))
# if get_xy_val(x,y) == None:
#     print('create a location ! ')
# else:
#     print('bad if')

turn_num = 60
def get_xy_val(x, y):
    xy = '{}_{}'.format(x, y)
    location = turns_dict.get(xy)
    if location == None:
        print('creating location ! ')
        # set x y values. checck visit flag
        turns_dict.update({xy: 0})
        turns_dict.update({xy: {'int_x': x, 'int_y': y, 'vis_his': turn_num}})
        return {xy: location}
    return {xy: location}


turn_num = 0
print('==========turn 0============')
def get_xy_val(x, y): # запрашивает x y, если такой локи нет создает либо
    xy = '{}_{}'.format(x, y) # отображает локу с turns_dict
    if xy in turns_dict.keys():
        vis_his_tmp = turns_dict.pop(xy)['vis_his']
        vht2_all = []
        for vht1 in vis_his_tmp:
            vht2_all.extend([vht1])
        vht2_all.append(turn_num)
        turns_dict.update({xy: {'int_x': x, 'int_y': y, 'vis_his': vht2_all}})
        return {xy: turns_dict.get(xy)}
    turns_dict.update({xy: {'int_x': x, 'int_y': y, 'vis_his': [turn_num]}})
    print('Location', x, y, 'created')
    return {xy: turns_dict.get(xy)}

turn_num = 1
print(get_xy_val(x, y))
print(turns_dict)
print(get_xy_val(x, y))
cur_turn_d = get_xy_val(x, y)

turn_num = 2

cur_turn_d = json.loads(open(ffile_in).read())
print(cur_turn_d)
turns_dict.update(cur_turn_d)

turn_num = 3

turns_dict = init_dict(ffile_in)

turn_num = 4

x = 5
y = 10
get_xy_val(x, y)

turn_num = 9999
get_xy_val(6, 10)
print(get_xy_val(6, 10))

turn_num = 5
get_xy_val(0, 0)
turn_num = 6
print(get_xy_val(0, 1))
turn_num = 7
print(get_xy_val(1, 0))
turn_num = 8
print(get_xy_val(0, 0))
turn_num = 9
print(get_xy_val(6, 10))
turn_num = 10
print(get_xy_val(7, 0))
turn_num = 11
print(get_xy_val(8, 10))
turn_num = 12
print(get_xy_val(8, 10))
turn_num = 13
print(get_xy_val(8, 10))
turn_num = 14
print(get_xy_val(8, 10))

print(xy, 'debug')
xy = '8_10'
if xy in turns_dict.keys():
    a = turns_dict.get(xy)['vis_his']
    print(a)

wr_dict()

turn_num = 0

aling = 0

def aply_path():
    print(turn_num)
    print(aling)
    print('aplypathfunc')
    count = 0
    for item in path_src:
        print(item[0])
        aling_src = item[0]
        if (aling_src == 'L'):
            aling -= 90
            count += 1
        if (aling_src == 'R'):
            aling += 90
            count += 1
        if aling == 360: aling = 0
        if aling == -90: aling = 0
        range_src = (item[1:len(item)])
        print(count, aling, range_src)
        print(item, '=========== WARRRRRP')
         # print(warp_range(aling, range_src, turn_num))
    return aling

print(aling)
path_src = ('L5', 'R123')
aply_path()
print(aling)

# , 'L5', 'L1', 'R5', 'R1', 'R1', 'L4', 'L1')
