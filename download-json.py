import requests
import json
req = requests.get('https://opendata.ecdc.europa.eu/covid19/casedistribution/json')

jobj = json.loads(req.content)

from collections import Counter
c = Counter()

for row in jobj['records']:
	country = row['countriesAndTerritories']
	death = int(row['deaths'])
	c[country]+= death

