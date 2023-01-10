BACKGROUND_COLOR = "#B1DDC6"

import smtplib
import pandas
import datetime as dt


PLACEHOLDER="[NAME]"
EMAIL="my_email@gmail.com"
PASSWORD="my_password"

df=pandas.read_csv("birthdays.csv")
#print(df)

now=dt.datetime.now()
month=now.month
day=now.day

for i in range(0,5):
    mob=df.at[i,"month"]
    dob=df.at[i,"day"]
    bod_e=df.at[i,"email"]
    bod_name=df.at[i,"name"]

if day == dob and month == mob:
    for i in range(1, 3):
        with open(f"letter_{i}.txt", "r") as letter_i:
            letter = letter_i.read()
            new_letter = letter.replace(PLACEHOLDER, bod_name)

    with smtplib.SMTP(EMAIL) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=bod_e,msg=f"Subject:Happy Birthday\n\n {new_letter}")

else:
    pass
