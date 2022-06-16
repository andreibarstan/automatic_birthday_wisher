# when this program runs, it check if current day matches a birthday, as per data stored in a .csv file.
# If it does, an email is automatically generated (based on email templates) and sent to the email address coresponding the matching birthday date.
# this code can be hosted in the cloud with pythonanywhere and it can be scheduled as a task to automatically run daily

import os
import smtplib
import datetime as dt
import random
import pandas

now = dt.datetime.now()  # current date/time
cur_day = now.day  # gets int (0 for monday, 2 for wednesday...)
cur_month = now.month

# open birthday.csv file
data = pandas.read_csv("birthdays.csv")  # open file
paired_data = data.to_dict(orient="records")  # transform data to dictionary and arrange(orientate) records as pairs
#print(paired_data)

for i in paired_data: # for each array of key-value pairs
    day = i['day'] # extract values of specific columns
    month = i["month"]
    name = i["name"]
    email = i["email"]
    if day == cur_day and month == cur_month: # if the current date matches a birthday
        file = random.choice(os.listdir("letter_templates")) # randomly choose a letter file
        #file_path = f"letter_templates/letter_{random.randint(1,3)}.txt" randomly choose a letter file according to name
        with open(f"letter_templates/{file}") as letter: # open letter
            final_letter = letter.read() # read and format letter
            final_letter = final_letter.replace("[NAME]", name)

        # send the email containing the formatted letter
        my_email = "*" # add sender email address
        password = "*" # add 16 char password for the email address - use app passwords from google account/security
        connection = smtplib.SMTP("smtp.gmail.com")  # SMTP object providing server name
        with smtplib.SMTP("smtp.gmail.com") as connection:  # with iteration also closes the connection automatically at the end
            connection.starttls()  # Transport Layer Security enables encryption and secures connection
            connection.login(user=my_email, password=password)  # login to my email domain
            connection.sendmail(from_addr=my_email,  # sender and recipient details, subject and message
                                to_addrs=email,
                                msg=f"Subject: Happy b-day!\n\n{final_letter}")
        print("Birthday email sent!")

