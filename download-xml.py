import requests
import xml.etree.ElementTree as ET

reqXML = requests.get('https://opendata.ecdc.europa.eu/covid19/casedistribution/xml')

tree = ET.fromstring(reqXML.content) 

from collections import Counter 
c = Counter()

for record in tree:
	country = 'unknown'
	deaths = 0
	for item in record:
		if item.tag == 'countriesAndTerritories':
			country = item.text
		if item.tag == 'deaths':
			deaths = int(item.text)
	c[country] += deaths

print(c)

death = 0
for item in tree.iter('deaths'): 
	death+= int(item.text) 

print (death)