#Will accept json where the keys are item_ids
#Will return the json with ids converted to item names

import sys
from urllib.request import urlopen
import json

#Repository of item ids and names
name_dict = json.loads(urlopen('https://raw.githubusercontent.com/ffxiv-teamcraft/ffxiv-teamcraft/master/libs/data/src/lib/json/items.json').read())

input_json = json.load(sys.stdin)
output_dict = {}

for item in input_json:
    item_name =  name_dict[item]['en']
    output_dict[item_name] = input_json[item]

output_json = json.dumps(output_dict)
print(output_json)
