import requests 

req = requests.get('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')

len(req.content)

# import os 
# os.getcwd() current working directory 

lines = req.content.decode(encoding='utf-8').replace("\\r", "").split('\\n')

fp = open('covid-19.csv', 'w')

for line in lines:
	x = fp.write(line + '\n')

fp.close()

import csv

reader = csv.DictReader(open('covid-19.csv'))
from collections import Counter
c = Counter()

for row in reader:
	country = row['countriesAndTerritories']
	death = int(row['deaths'])
	c[country]+= death


writer = csv.DictWriter(open('covid-19-deaths.csv', 'w'), fieldnames = ['country', 'number_of_deaths'])

writer.writeheader()
for k in c.keys():
	writer.writerow({'country': k, 'number_of_deaths' : c[k]})