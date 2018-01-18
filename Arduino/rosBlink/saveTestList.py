import simplejson
import json
#listTest = [1, 2, 8]
#f = open('output.txt', 'w')
#simplejson.dump(listTest, f)
#f.close()

json1 = open('ut.json', 'w')
json1_obj = json.load(json1)

for i in json1_obj['data']:
    ip = [i['custom3']['modemId']]