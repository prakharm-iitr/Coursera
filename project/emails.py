#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes
import smtplib
import os

def generate_email(sender, recipient, subject, body, attachment_path):
	message = EmailMessage()
	message['From'] = sender
	message['To'] = recipient
	message['Subject'] = subject
	message.set_content(body)

	file_name = os.path.basename(attachment_path)
	mimetype , _ = mimetypes.guess_type(file_name)
	m_type, m_subtype = mimetype.split('/',1)

	with open(attachment_path, 'rb') as f:
		message.add_attachment(f.read(), 
			maintype= m_type, subtype= m_subtype, filename= file_name)

	return message

def generate_error_email(sender, recipient, subject, body):
	message = EmailMessage()
	message['From'] = sender
	message['To'] = recipient
	message['Subject'] = subject
	message.set_content(body)

	return message

def send_email(message):
	mail_server = smtplib.SMTP('localhost')
	mail_server.send_message(message)
	mail_server.quit()