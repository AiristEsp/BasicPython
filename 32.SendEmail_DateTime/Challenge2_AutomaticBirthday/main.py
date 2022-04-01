##################### Extra Hard Starting Project ######################
import pandas
from datetime import datetime
import random
import smtplib

MY_EMAIL = "smtp@gmail.com"
MY_PASSWORD = "@"


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tupple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)

if today_tupple in birthdays_dict:
    birthday_person = birthdays_dict[today_tupple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(contents)

# # 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL, 
            to_addrs = "vinmoza01@gmail.com", 
            msg =f"Subject:Happy Birthday!\n\n{contents}"
        )
        connection.close()



