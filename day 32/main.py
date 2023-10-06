# import smtplib
# my_email = "mirzanmiraj@yahoo.com"
# passwrd = "AYSHAMANZIL "
# connection = smtplib.SMTP("smtp.mail.yahoo.com")
# connection.starttls()
# connection.login(user=my_email, password=passwrd)
# connection.sendmail(from_addr=my_email, to_addrs="mirzan.testing@gmail.com", msg="hello")
# connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year

print(year)
