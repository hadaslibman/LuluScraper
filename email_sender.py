import smtplib
import json

with open ("secrets.json", "r") as f:
    secrets = json.load(f)
    gmail_user = secrets["mail"]["user"]
    gmail_password = secrets["mail"]["password"]

def send_email(body):
    sent_from = gmail_user
    to = ['hadaslibman@gmail.com']
    subject = 'WOOHOO GO FIND YOUR CARD!!!'


    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()


    print ('Email sent!')

