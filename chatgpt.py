import openai
import smtplib
from email.mime.text import MIMEText
# A simple Python program to demonstrate
# getpass.getpass() to read password
import getpass
import pdb; pdb.set_trace()
un = getpass.getuser()
try:
	pw = getpass.getpass()
except Exception as error:
	print('ERROR', error)
else:
	print('Password entered:', len(pw))

apikey = open("apikey.txt").read()
openai.api_key = apikey

def send_email(to_email, from_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create the email message
    msg = MIMEText(body)
    msg['To'] = to_email
    msg['From'] = from_email
    msg['Subject'] = subject

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, msg.as_string())

    print('Email sent successfully.')

def handle_message(message):
    # Define email parameters
    to_email = 'kishor.ruc@gmail.com'
    from_email = 'kishor.rvc.mvit@gmail.com'
    subject = 'ChatGPT Interaction Summary'
    body = 'Here is a summary of your interactions with ChatGPT: ...'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = un
    smtp_password = pw

    # Send email on user request
    if message.lower() == 'send me a summary email':
        send_email(to_email, from_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password)
        return 'Okay, I have sent you a summary email.'
    
    # Handle other user requests and interactions here...
    
    # If the message doesn't match any known requests, respond with a default message
    return 'I didn\'t understand that. Can you please try again?'

while True:
    user_input = input('You: ')
    response = handle_message(user_input)
    print('ChatGPT:', response)
