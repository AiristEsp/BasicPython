import smtplib

my_email = "email@gmail.com"
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="vinmoza01@gmail.com", 
        msg="Subject:Hello\n\nhello")
    connection.close()