#!/usr/bin/env python3

import os, socket, psutil
import emails

def check():
	error_code = []
	if psutil.cpu_percent()>80.0:
		error_code.append("CPU usage is over 80%")
	if psutil.disk_usage('/').percent < 20.0:
		error_code.append("Available disk space is less than 20%")
	if psutil.virtual_memory().available < 500* 2**20 :
		error_code.append("Available memory is less than 500MB")
	if not socket.gethostbyname('localhost') == '127.0.0.1':
		error_code.append("localhost cannot be resolved to 127.0.0.1")
	return error_code

if __name__ == '__main__':
	error_code = check()

	if error_code:
		sender = "automation@example.com"
		receiver = "{}@example.com".format(os.environ.get('USER',''))
		body = "Please check your system and resolve the issue as soon as possible"
		for error in error_code:
			subject = "Error - {}".format(error)
			msg = emails.generate_error_email(sender, receiver, subject, body)
			emails.send_email(msg)