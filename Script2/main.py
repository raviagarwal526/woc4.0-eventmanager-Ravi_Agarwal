import smtplib
import csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import Message
import getpass

def read_template(filename):
    with open(f'E:\WoC\Script2\Send_email_using_python\{filename}', 'r', encoding="utf-8") as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

MY_ADDRESS = input('Enter your email:')
PASSWORD = getpass.getpass()

# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()   
s.login(MY_ADDRESS, PASSWORD)
 
with open("E:\WoC\Script2\Send_email_using_python\details.csv") as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  next(csv_reader)
  for row in csv_reader:
    msg = MIMEMultipart() # create a message
    message_template = read_template('template.txt')
    message = message_template.substitute(PERSON_NAME=row[0],DSA=row[2],CS=row[3],MATHS=row[4])
    print(message)
    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=row[1]
    msg['Subject']="Mid term grades"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg
 
s.quit()
