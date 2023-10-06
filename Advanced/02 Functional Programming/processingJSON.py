import json
from collections import namedtuple
from functools import reduce

city = namedtuple("city", ["name", "country", "coordinates", "continent"])

with open('cities.json') as json_file:
  data = json.load(json_file) 

cities = map(lambda x: city(x["name"], x["country"], x["coordinates"], x["continent"]), data["city"])

'''
Store all cities that are on the continent of Asia in the tuple called asia. Make sure to print out your result.
'''
# Code for Checkpoint 1 goes here.
asia = tuple(filter(lambda x: x.continent=='Asia', cities))
print(asia)

'''
Find the western-most city in the asia tuple and store it in the west variable. Make sure to print out your result.

Note: the western-most country is the one where the longitude is the lowest number (minimum of city.coordinates[1])
'''
# Code for Checkpoint 2 goes here.
west = reduce(lambda x,y: x if x.coordinates[1]<y.coordinates[1] else y, asia)
print('---')
print(west)
#print(west.name)