import json
import os

loc=[]
with open('bzerp.json') as f:
    coordinate_for_json = json.load(f)

#print(coordinate_for_json)

for section, commands in coordinate_for_json.items():
    geometry=commands[0]
spisok_coordinate=geometry['geometry']['coordinates']

for coordanate in spisok_coordinate:
    latitude_for_route=coordanate[0]
    longitude_for_route=coordanate[1]
    #print(latitude_for_route)
    #print(longitude_for_route)
    loc.append((latitude_for_route, longitude_for_route))


print(loc)
