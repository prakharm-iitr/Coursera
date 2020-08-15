#!/usr/bin/env python3

import os, requests

#wd = "/home/{}/supplier-data/descriptions/".format(os.environ.get("USER",""))
wd = "./supplier-data/descriptions/"
url = "http://-------/fruits"
#keys = ['name', 'weight', 'description', 'image_name']

for item in os.listdir(wd):
	item_path = os.path.join(wd,item)
	item_name, ext = os.path.splitext(item)

	if os.path.isfile(item_path):
		fruit_data = {}

		with open(item_path) as f:
				fruit_data['name'] = f.readline().strip()
				fruit_data['weight'] = f.readline().strip('\n lbs')
				fruit_data['description'] = f.readline().strip()
				fruit_data['image_name'] = item_name+'.jpeg'

		print(fruit_data)
		r = requests.post(url, data= fruit_data)