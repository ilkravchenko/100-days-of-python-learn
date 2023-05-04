import pandas as pd
import datetime as dt
import smtplib
import random

##################### Extra Hard Starting Project ######################
letters = ['./letter_templates/letter_1.txt', './letter_templates/letter_2.txt', './letter_templates/letter_3.txt']
file_path = f'./letter_templates/letter_{random.randint(1, 3)}.txt'

MY_EMAIL = "bilbob172839@gmail.com"
PASSWORD = "bswxpubchiudxhwi"

# 1. Update the birthdays.csv

birthdays_df = pd.read_csv('./birthdays.csv')
birthdays = birthdays_df.to_dict(orient='records')

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
month = now.month
day = now.day

for person in birthdays:
    if person['month'] == month and person['day'] == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        random_letter = random.choice(letters)
        person_email = person['email']
        person_name = person['name']
        with open(random_letter, 'r') as file:
            letter = file.read()
            letter = letter.replace('[NAME]', person_name)

        # 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=person_email,
                                msg=f"Subject:Happy Birthday!\n\n{letter}")
