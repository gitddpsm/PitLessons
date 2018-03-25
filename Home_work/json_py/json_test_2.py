import io ,json

json_data = open('new_data.json').read()

data = json.loads(json_data)
print(data)
print(json.loads(json_data)['persons'][1])

print(json.loads(json_data)['path_map'][0]['xy'])
print(json.loads(json_data)['path_map'][0]['turn_hist'])
print(len(json.loads(json_data)['path_map'][0]['turn_hist']))

tmp = json.loads(json_data)['path_map'][0]['turn_hist']
json.loads(json_data)['path_map'][0]['turn_hist'] = (0, 1, 2, 3)
print(json.loads(json_data)['path_map'][0]['turn_hist'])

# json_data = '{"name": "Brian", "city": "Seattle"}'
python_obj = json.loads(json_data)
print(json.dumps(python_obj, sort_keys=True, indent=4))

print(data["persons"][1])

for item in data['path_map']:
    print('data =', data)
    print('= data[item] =', item['xy'])
    print(len(item['turn_hist']))

print(json.loads)

print('j data', json_data)

    # if data[item] == 'xy':
    #     print(item['xy'], '= print X and Y')

    # for sub_item in item:
    #     print('item =',item, ', sub item =',sub_item)

