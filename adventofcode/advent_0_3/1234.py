print("1234")

import json

ffile_in = '2703_data_3.0.1.json'

def wr_dict():
    with open(ffile_in, 'w') as ffile:
        json.dump(turns_dict, ffile, sort_keys=True, indent=4)

def init_dict(ffile_in):
    try:
        json_input = open(ffile_in).read() #    откр фл на чтение
        turns_dict = json.loads(json_input) #  модулем json всасываем открытый файл
        print(turns_dict.get('ver'), 'loaded ver') # тестируем словарь,
        ver = turns_dict.get('ver') + 1
        turns_dict = {}
        turns_dict.update({'ver': ver})
        wr_dict()
    except:
        turns_dict = {}
        with open(ffile_in, 'w') as ffile:
            turns_dict.update({'ver': 0})
            json.dump(turns_dict, ffile, sort_keys=True, indent=4)
    return turns_dict


turn_num = 0
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


ffile_in = '2703_data_3.0.1.json'
print(init_dict(ffile_in))
turns_dict = init_dict(ffile_in)
print(turns_dict)
elcord = '0_0'
el_x = 0
el_y = 0
el_hist = 0

get_xy_val(el_x, el_y)

turn_num = 5
get_xy_val(0, 0)
turn_num = 6
print(get_xy_val(0, 1))
turn_num = 7
print(get_xy_val(200, 250))
turn_num = 8

print(turns_dict)

wr_dict()

50 * 60

#

