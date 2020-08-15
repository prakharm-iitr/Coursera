#!/usr/bin/env python3

import os
from PIL import Image

# wd = "/home/{}/supplier-data/images/".format(os.environ.get('USER',""))
wd = "./supplier-data/images"

for item in os.listdir(wd):
	item_path = os.path.join(wd,item)
	item_name, ext = os.path.splitext(item)

	if os.path.isfile(item_path):
		with Image.open(item_path) as im:
			new_im = im.convert("RGB").resize((600,400))
			new_name = item_name + ".jpeg"
			new_im.save(os.path.join(wd,new_name))
