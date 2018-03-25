# HOly Bunny
import json
import io

path_src = ('L5', 'R1', 'L5', 'L1', 'R5', 'R1', 'R1', 'L4', 'L1', 'L3', 'R2', 'R4', 'L4', 'L1', 'L1', 'R2', 'R4', 'R3', 'L1'
        , 'R4', 'L4', 'L5', 'L4', 'R4', 'L5', 'R1', 'R5', 'L2', 'R1', 'R3', 'L2', 'L4', 'L4', 'R1', 'L192', 'R5', 'R1',
        'R4', 'L5', 'L4', 'R5', 'L1', 'L1', 'R48', 'R5', 'R5', 'L2', 'R4', 'R4', 'R1', 'R3', 'L1', 'L4', 'L5', 'R1',
        'L4', 'L2', 'L5', 'R5', 'L2', 'R74', 'R4', 'L1', 'R188', 'R5', 'L4', 'L2', 'R5', 'R2', 'L4', 'R4', 'R3', 'R3'
        , 'R2', 'R1', 'L3', 'L2', 'L5', 'L5', 'L2', 'L1', 'R1', 'R5', 'R4', 'L3', 'R5', 'L1', 'L3', 'R4', 'L1', 'L3',
            'L2', 'R1', 'R3', 'R2', 'R5', 'L3', 'L1', 'L1', 'R5', 'L4', 'L5', 'R5', 'R2', 'L5', 'R2', 'L1', 'L5', 'L3',
            'L5', 'L5', 'L1', 'R1', 'L4', 'L3', 'L1', 'R2', 'R5', 'L1', 'L3', 'R4', 'R5', 'L4', 'L1', 'R5', 'L1', 'R5',
            'R5', 'R5', 'R2', 'R1', 'R2', 'L5', 'L5', 'L5', 'R4', 'L5', 'L4', 'L4', 'R5', 'L2', 'R1', 'R5', 'L1', 'L5', 'R4'
        , 'L3', 'R4', 'L2', 'R3', 'R3', 'R3', 'L2', 'L2', 'L2', 'L1', 'L4', 'R3', 'L4', 'L2', 'R2', 'R5', 'L1', 'R2')

# path_src = ('R8', 'R4', 'R4', 'R8')

pos_x = 0
pos_y = 0
angle = 0  # 0 - North;90 - East; 180 - South; 270 - West
turn_num = 0

path_dict = {}
# loc_name = str('{}_{}'.format(pos_x,pos_y))
path_dict[str('{}_{}'.format(pos_x,pos_y))] = {'x': pos_x, 'y': pos_y, 'turn_hist': [0]}
# path_dict['turn_hist'] = [0]

def setAngle(current, alpha):
    if alpha == 'L':
        current -= 90
    if alpha == 'R':
        current += 90
    if current == 360:
        current = 0
    if current == -90:
        current = 270
    return current


for act_src in path_src:
    turn = act_src[0]
    # print(turn)
    move_rng = int(act_src[1:len(act_src)])
    # print(move_rng)
    angle = setAngle(angle, turn)
    if angle == 90:
        pos_x += move_rng
        print('East')
    if angle == 270:
        pos_x -= move_rng
        print('West')
    if angle == 0:
        print('North')
        pos_y += move_rng
    if angle == 180:
        print('South')
        pos_y -= move_rng
    turn_num += 1
    path_key = '{}_{}'.format(pos_x,pos_y)
    if path_dict.get(path_key) == None:
        path_dict[str('{}_{}'.format(pos_x,pos_y))] = {'x': pos_x, 'y': pos_y, 'turn_hist': [turn_num]}
    else:
        history_list = path_dict.get(path_key)['turn_hist'][0], (turn_num)
        print('History list! =', history_list, turn_num)
        path_dict[str('{}_{}'.format(pos_x,pos_y))] = {'x': pos_x, 'y': pos_y, 'turn_hist': history_list}
    print(pos_x, pos_y, 'turn =', turn_num)



print(pos_x, ' ',   pos_y)
print(pos_y + pos_x)

print(path_dict)
with open('path_raw.json', 'w') as ext_file:
    json.dump(path_dict, ext_file, sort_keys=False, indent=4)

