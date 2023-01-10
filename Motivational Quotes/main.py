import pandas
import random
import smtplib
import datetime as dt

#PLEASE PUT THE DETAILS OF THE EMAIL HERE
EMAIL="example1@gmail.com"
PASSWORD="example@123"
RECIPIENT_EMAIL="example2@gmail.com"

INDEX=random.randint(0,101)
df=pandas.read_csv("quotes.txt")
select=df.iloc[INDEX]
#print(select)


now=dt.datetime.now()
day=now.weekday()

#This will send a quote every monday || We can alter the sender and recipient by changing the emails
if day==0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        email =EMAIL
        password = PASSWORD
        recipient=RECIPIENT_EMAIL
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=recipient, msg=f"Subject:motivational Quotes\n\n{select}")
else:
    pass


