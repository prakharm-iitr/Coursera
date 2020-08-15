#!/usr/bin/env python3

import os, datetime
import reports
import emails

"""Change wd"""
# wd = "/home/{}/supplier-data/descriptions/".format(os.environ.get("USER",""))
wd = "./supplier-data/descriptions/"
data = []

for item in os.listdir(wd):
	item_path = os.path.join(wd,item)
	if os.path.isfile(item_path):
		with open(item_path) as f:
			data.append("name: {}<br/>weight: {}".format(
				f.readline().strip(), f.readline().strip()))

report_data = "<br/><br/>".join(data)
title = "Processed Update on {}".format(datetime.datetime.now().strftime('%x'))

if __name__ == '__main__':
	"""Change file location to /tmp/processed.pdf"""
	reports.generate_report('./processed.pdf', title, report_data)

	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get('USER',""))
	subject = 'Upload Completed - Online Fruit Store'
	body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
	attach_file = '/tmp/processed.pdf'

	message = emails.generate_email(sender, receiver, subject, body, attach_file)
	emails.send_email(message)