import json, datetime

fp = open('earthquake.json','r')
earthquakes = json.load(fp)

print("earthquake information：")
for eq in earthquakes['features']:
    print("place:{}".format(eq['properties']['place']))
    print("magnitude:{}".format(eq['properties']['mag']))
    et = float(eq['properties']['time']) /1000.0
    print("time:{}".format(et))
