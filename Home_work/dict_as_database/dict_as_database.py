datastore = { "office": {
    "medical": [
        { "room-number": 100,
          "use": "reception",
          "sq-ft": 50,
          "price": 75
          },
        { "room-number": 101,
          "use": "waiting",
          "sq-ft": 250,
          "price": 75
          },
        { "room-number": 102,
          "use": "examination",
          "sq-ft": 125,
          "price": 150
          },
        { "room-number": 103,
          "use": "examination",
          "sq-ft": 125,
          "price": 150
          },
        { "room-number": 104,
          "use": "office",
          "sq-ft": 150,
          "price": 100
          }
    ],
    "parking": {
        "location": "premium",
        "style": "covered",
        "price": 750
    }
}
}

print(datastore["office"]["parking"])
print(datastore["office"]["medical"][0])
print(datastore["office"].get("law"))

spaces = datastore['office']['medical']
print(spaces)

for item in spaces:
    if item.get('use') == "examination":
        item['price'] = 175

for item in datastore['office']['medical']:
    print(item)
    print(item.get('use'),' it is usage of item')
    if item.get('use') == "examination":
        print('The {} rooms now cost {}'.format(item.get("use"), item.get("price")))