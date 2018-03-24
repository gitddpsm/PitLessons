
# turn_history = {'number' : 1 , {'location' : {'pos_x': 0, 'pos_y': 0}}}

person = {
    'name' : {'last_name': 'Ivanov', 'first_name': 'Ivan'},
    'address': ['Andrushki city', 'vasilkovskaya str 23' , 'kv.12'],
    'phone': {'home_phone': '8-123-456456', 'mob_phone' : '8-904-2126390'},
    'integer': 1
    }

print(person['integer'])

person = {}
person.fromkeys(('first_name', 'last_name'))
print(person)
person = person.fromkeys(('first_name', 'last_name'), 'Jack')
print(person.get('first_name'))

coordinates = {'11.12':{'pos_x':11,'pos_y':12}}
coordinates = {'12.12':{'pos_x':12,'pos_y':12}}

myTrace = [[0 for x in range(100)] for y in range(100)]

myTrace[0][0] = {'pos_x':0,'pos_y':0, 'is_visited': True}
myTrace[-10][-15] = {'pos_x': (-10),'pos_y': (-15), 'is_visited': True}


print(myTrace[0][0]['is_visited'])

# myTrace.insert(-10, -15)
print(myTrace[-10][-15])


# index по номеру хода
myTrace_turn = {0: {'x': 5, 'y': 3}}
myTrace_turn.update({1: {'x': 4, 'y': 3}})

# index по координате
myTrace_cord = myTrace_turn.get(0)['x']

print(myTrace_cord)
print(myTrace_turn)

my_x = 1
my_y = 3
is_Visit = True
turn_num = 2

myTrace_turn_update = {
    (str(my_x) + '_' + str(my_y)): {
    'turn_num': turn_num,
    'x': my_x,
    'y': my_y,
    'is_visited': True
    }}

print(myTrace_turn_update)
myTrace_turn.update(myTrace_turn_update)
print(myTrace_turn.get('1_3')['is_visited'])

if (myTrace_turn.get((str(my_x) + '_' + str(my_y)))['is_visited']) == True:
    print(
        myTrace_turn.get((str(my_x) + '_' + str(my_y)))['turn_num']
        )

    myTrace_turn.get(
        (str(my_x) + '_' + str(my_y)))['turn_num'] = myTrace_turn.get((str(my_x) + '_' + str(my_y)))['turn_num'],turn_num

    print(
        myTrace_turn.get((str(my_x) + '_' + str(my_y)))['turn_num']
        )

print(myTrace_turn.get((str(my_x) + '_' + str(my_y)))['turn_num'])

