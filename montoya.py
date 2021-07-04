import json
import requests
import time
import csv
from bs4 import BeautifulSoup
url_prefix = "https://slco.org/services/tr/tr-delinquent-service/api/v1/Delinquent/GetDelinquent/"

last_char = ("1","a",) # "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
last_char2 = ("1","a")
rawlist = []
datalist1 = []

from CF.SUBM_D import _01_DEBUG as DBG


#scrap deleqint list
counter = 0
for char in last_char:
	full_url = url_prefix + char
	r = requests.get(full_url)
	time.sleep(.5)
	counter += 1
	if (
			()
	):
		.
	print(counter, "of", len(last_char), r.status_code)
	_TItem_ = r.json()["data"]
	# here is where to strip spaces soon as I get your data complete I will come back and see what I can do here to speed and eat less memory at a time
	# also as soon as you are done with r:
	del r
	rawlist.extend(_TItem_)


#remove extra parent list
#for a in rawlist:
#	print(f"""a {a}""")
#	for b in a:
#		datalist1.append(b)
datalist1.extend(rawlist)
print(f"""
datalist1
{datalist1}
datalist1
{DBG.IGMPP(datalist1)}
""")
#with (
#		(open("datalist1.json", "tw")) as FD_out,
#		(open("rawlist.json", "tw")) as FD_out1
#):
#	FD_out.write(DBG.myPp(datalist1))
#	FD_out1.write(DBG.myPp(rawlist))
exit()

#remove whitespace from name
for a in datalist1:
	for b in a :
		if b == "ownerName":
			c = a[b]
			a[b] = c.strip()
# Create list of ids
id_list = [a["parcelNumber"] for a in datalist1]

print("got ID list")

# scrape each parcel url
datalist2 = []
counter = 0
for ID in id_list:
		data = {"parcelid":ID}
		url_seed = 'https://slco.org/assessor/new/resultsMain.cfm'
		x = requests.post(url_seed, data)
		counter += 1
		print("got html for Property",counter,"of",len(id_list))
		url = x.url
		y = x.text
		soup2 = BeautifulSoup(y, "html.parser")
		tb_list = soup2.find_all("tbody")
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
