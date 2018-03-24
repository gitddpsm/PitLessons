# HOly Bunny

path_src = ('L5', 'R1', 'L5', 'L1', 'R5', 'R1', 'R1', 'L4', 'L1', 'L3', 'R2', 'R4', 'L4', 'L1', 'L1', 'R2', 'R4', 'R3', 'L1'
        , 'R4', 'L4', 'L5', 'L4', 'R4', 'L5', 'R1', 'R5', 'L2', 'R1', 'R3', 'L2', 'L4', 'L4', 'R1', 'L192', 'R5', 'R1',
        'R4', 'L5', 'L4', 'R5', 'L1', 'L1', 'R48', 'R5', 'R5', 'L2', 'R4', 'R4', 'R1', 'R3', 'L1', 'L4', 'L5', 'R1',
        'L4', 'L2', 'L5', 'R5', 'L2', 'R74', 'R4', 'L1', 'R188', 'R5', 'L4', 'L2', 'R5', 'R2', 'L4', 'R4', 'R3', 'R3'
        , 'R2', 'R1', 'L3', 'L2', 'L5', 'L5', 'L2', 'L1', 'R1', 'R5', 'R4', 'L3', 'R5', 'L1', 'L3', 'R4', 'L1', 'L3',
            'L2', 'R1', 'R3', 'R2', 'R5', 'L3', 'L1', 'L1', 'R5', 'L4', 'L5', 'R5', 'R2', 'L5', 'R2', 'L1', 'L5', 'L3',
            'L5', 'L5', 'L1', 'R1', 'L4', 'L3', 'L1', 'R2', 'R5', 'L1', 'L3', 'R4', 'R5', 'L4', 'L1', 'R5', 'L1', 'R5',
            'R5', 'R5', 'R2', 'R1', 'R2', 'L5', 'L5', 'L5', 'R4', 'L5', 'L4', 'L4', 'R5', 'L2', 'R1', 'R5', 'L1', 'L5', 'R4'
        , 'L3', 'R4', 'L2', 'R3', 'R3', 'R3', 'L2', 'L2', 'L2', 'L1', 'L4', 'R3', 'L4', 'L2', 'R2', 'R5', 'L1', 'R2')


pos_x = 0
pos_y = 0
angle = 0  # 0 - North;90 - East; 180 - South; 270 - West


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

# dict with a number of turn, and arrival cords ?
# turn_history = {'number', {'location' : {'pos_x': 0, 'pos_y': 0}}, {'visit_num' : 1 }}

# dict with a number of turn, and target cords ?

for act_src in path_src:
    turn = act_src[0]
    print(turn)
    move_rng = int(act_src[1:len(act_src)])
    print(move_rng)
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
    print(pos_x, ' ',   pos_y)

print(pos_x, ' ',   pos_y)
print(pos_y + pos_x)



