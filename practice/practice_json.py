import json

fp = open('students.json','r')
records = json.load(fp)
#print(records)

for record in records:
	print('name: {}, math score:{}, english score:{}'.format(record['name'], \
	record['report'][0]['score'], \
	record['report'][1]['score'], \
	
	))
