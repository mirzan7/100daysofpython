import datetime as dt
import requests

MY_LAT = 13.0878
MY_LONG = 80.2785
parameter = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}
response = requests.get("https://api.sunrise-sunset.org/json? , ", params=parameter)
response.raise_for_status()
data = response.json()
print(data)
now = dt.datetime.now()
print(now)