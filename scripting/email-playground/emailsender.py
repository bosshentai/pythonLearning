import smtplib
from email.message import EmailMessage
from string import Template
from  pathlib import Path

email = EmailMessage()
email['from'] = 'Hernani Baptista'
email['to'] = 'baptistamhernani@gmail.com'
email['subject'] = 'Pegam na ov'

email.set_content('I am learning Python ')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'password')
    smtp.send_message(email)
    print('all good boss!')