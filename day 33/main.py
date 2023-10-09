import datetime as dt
import requests
import smtplib
import time

MY_LAT = 13.0878
MY_LONG = 80.2785
MY_EMAIL = ""
MY_PASSWORD = ""
MY_ANOTHER_EMAIL = ""


def is_iss_near():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if MY_LAT - 5 < iss_lat < MY_LONG + 5 and MY_LONG - 5 < iss_lng < MY_LONG + 5:
        return True


def is_night():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_near() and is_night():
        connection = smtplib.SMTP("smtp.mail.yahoo.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_ANOTHER_EMAIL,
            msg = "Subject:Look Up \n\n the iss is above you in the sky"
        )