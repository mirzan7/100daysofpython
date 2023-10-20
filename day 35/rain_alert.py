import requests

api_key = "f4c266e099a12f1bc1df0b5a1283be51"

parameters = {
    "lat": 33.44,
    "lon": -94.04,
    "exclude": "hourly",
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
print(response.json)
