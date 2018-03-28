# Map for puzzle path
# recive coords & turn number
import io, json

json_data = open('path_raw.json').read()
path_raw = json.loads(json_data)
# print(path_raw)
for item in path_raw:
    # print('item =', item ,path_raw[item])
    if len(path_raw[item]['turn_hist']) > 1:
        print(path_raw[item])
        print(path_raw[item]['x'] + path_raw[item]['y'])
print((91 - 71) + (135 - 82))