import requests
from twilio.rest import Client
will_rain = None
api_key = "f="
account_sid = '='
auth_token = '[AuthToken]'

parameters = {
    "lat": 13.08784,
    "lon": 80.27847,
    "APPID": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
weather_data = response.json
print(response.json)
weather_slice = weather_data["hourly"][:12]
print(weather_slice)
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="donot forget your umbrella today:)",
        from_='+14695138970',
        to='+91828*****'
    )
    print(message.status)

