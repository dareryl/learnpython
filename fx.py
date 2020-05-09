#!/Users/darylchan/opt/anaconda3/bin/python3


import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import csv
import pandas as pd
import datetime

if len(sys.argv) != 2:
    print('Usage: '+sys.argv[0]+' currency')
    exit(1)

currency = sys.argv[1]

main_url = 'https://api.exchangeratesapi.io/'
base = '?base='+currency

## Latest currency
today = datetime.date.today()
today_url = main_url + str(today) + base
r0 = requests.get(today_url, verify=False)
j0 = r0.json()
newrates = j0['rates']

## Previous currency
for i in range(1,31): 
    prev = today - datetime.timedelta(days=i)
    prev_url =  main_url + str(prev) + base 
    r1 = requests.get(prev_url, verify=False)
    j1 = r1.json()
    if j1 != j0: 
        break 
        
prevrates = j1['rates']

fp = open ('latest_currency.csv', 'w', encoding = "utf8", newline = '')
new_writer = csv.DictWriter(fp, fieldnames= ['Country','Rate to '+currency,'Rise/Fall','percentage change'])
new_writer.writeheader()
for row in newrates: 
    if row != currency :
        percent = ((prevrates[row] - newrates[row])/prevrates[row])*100
        if percent > 0 :
            new_writer.writerow({'Country': row,'Rate to '+currency: newrates[row], 'Rise/Fall': 'Rise', 'percentage change': "%.2f" % percent})
        if percent < 0: 
            new_writer.writerow({'Country': row,'Rate to '+currency: newrates[row], 'Rise/Fall': 'Fall', 'percentage change': "%.2f" % percent})      
fp.close()
df = pd.read_csv('latest_currency.csv')
