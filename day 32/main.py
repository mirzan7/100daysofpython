# import smtplib
# my_email = "mirzanmiraj@yahoo.com"
# passwrd = "1234567889*"
# connection = smtplib.SMTP("smtp.mail.yahoo.com")
# connection.starttls()
# connection.login(user=my_email, password=passwrd)
# connection.sendmail(from_addr=my_email, to_addrs="mirzan.testing@gmail.com", msg="hello")
# # connection.close()
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
#
# print(year)
import random
import smtplib
import datetime as dt
now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 5:
    with open("quotes.txt", 'r') as datafile:
        quotes = datafile.readline()
        random_quote = random.choice(quotes)
    my_email = "mirzanmiraj@yahoo.com"
    passwrd = "AYSHAMANZIL"
    connection = smtplib.SMTP("smtp.mail.yahoo.com")
    connection.starttls()
    connection.login(user=my_email, password=passwrd)
    connection.sendmail(from_addr=my_email, to_addrs="npmirzanmiraj5@gmail.com", msg=quotes)
