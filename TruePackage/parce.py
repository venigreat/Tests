import json
from pprint import pprint

with open('/Users/andrey.belyaev/Downloads/12.json') as json_data:
    d = json.load(json_data)
    list_ids={}
    for i in range (len(d['data'])):
        count = list_ids.get(d['data'][i]['id'])
        if count!= None:
            list_ids[d['data'][i]['id']]=count+1
        else:
            list_ids[d['data'][i]['id']] = 1

    print(list_ids)
