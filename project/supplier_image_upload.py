#!/usr/bin/env python3

import os, requests

wd = "/home/{}/supplier-data/images/".format(os.environ.get('USER',""))
url = "http://localhost/upload/"

for item in os.listdir(wd):
	item_name, ext = os.path.splitext(item)
	if ext == ".jpeg":
		with open(os.path.join(wd,item), 'rb') as im:
			r = requests.post(url, files={'file':im})