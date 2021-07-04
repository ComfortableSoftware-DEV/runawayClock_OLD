


import json
import requests
import time
import csv
from bs4 import BeautifulSoup
url_prefix = "https://slco.org/services/tr/tr-delinquent-service/api/v1/Delinquent/GetDelinquent/"


from CF.SUBM_D import _01_DEBUG as DBG

last_char = ("1","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
last_char2 = ("1","a")
rawlist = []
datalist1 = []

z = 0

def strip_all(x):
	if isinstance(x, str):
		x = x.strip()
	elif isinstance(x, list):
		x = [strip_all(v) for v in x]
	elif isinstance(x, dict):
		for k, v in x.iteritems():
			x.pop(k)
			x[ strip_all(k) ] = strip_all(v)
	return x

#scrap deleqint list
for char in last_char:
		full_url = url_prefix + char
		r = requests.get(full_url)
		z = z+1
		print(z , "of 27", r.status_code)
		time.sleep(.5)
		rawlist.append(r.json()['data'])
		print(f"""{DBG.getDebugInfo()}
IGMPP(r) {DBG.IGMPP(r)}
""")

#remove extra html info
for a in rawlist:
		for b in a:
				datalist1.append(b)

#remove whitespace from name
for a in datalist1:
	for b in a :
		if b == "ownerName":
			c = a[b]
			a[b] = c.strip()
# conver to csv sheet
#with open('test2.csv', 'w', newline='') as csvfile:
#    fieldnames = ['parcelNumber', 'ownerName','amount']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#    writer.writeheader()
#    writer.writerows(datalist)


# Create list of ids
id_list = []
for a in datalist1:
		id_list.append(a["parcelNumber"])

print(id_list)
print(datalist1)

# scrape each parcel url
datalist2 = []
for ID in id_list:
		dat = {"parcelid":ID}
		url_seed = 'https://slco.org/assessor/new/resultsMain.cfm'
		data = dat
		x = requests.post(url_seed, data)
		url = x.url
		y = x.text
		soup = BeautifulSoup(y, "html.parser")
		tb_list = soup.find_all("tbody")
		thraw = tb_list[0].find_all('th')
		tdraw = tb_list[0].find_all('td')
		th = []
		td = []
		th.append("url")
		td.append(url)
		for i in thraw:
				th.append(i.text)
		for i in tdraw:
				td.append(i.text)
		ary = dict(zip(th, td))
		datalist2.append(ary)
