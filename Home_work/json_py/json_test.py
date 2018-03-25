# import json
# json.dumps(['foo', {'bar': ('baz', None, 1.0, 2 )}]) # console command
# print(json.dumps("\"foo\bar"))

import io ,json

# строка которую будем парсить

json_string = """ {
  "orderID": 42,
  "customerName": "John Smith",
  "customerPhoneN": "555-1234",
  "orderContents": [
    {
      "productID": 23,
      "productName": "keyboard",
      "quantity": 1
    },
    {
      "productID": 13,
      "productName": "mouse",
      "quantity": 1
    }
  ],
  "orderCompleted": true
} """

# распарсенная строка
parsed_string = json.loads(json_string)
print(parsed_string)

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2 )}]) # console command
print(json.dumps("\"foo\bar"))

data = json_string
data2 = {'pos_x': 0, 'pos_y': 0, 'turn': {'is_vis': True, 'history': (0)}}

with open('data.json', 'w') as ext_file:
    json.dump(data, ext_file)
