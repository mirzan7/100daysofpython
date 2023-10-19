import requests

api_key = "f4c266e099a12f1bc1df0b5a1283be51"

parameters = {
    "lat": 11.9850509056689,
    "lon": 75.5559240883433,
    "appid": "f4c266e099a12f1bc1df0b5a1283be51",
}

response = requests.get(url="", params=parameters)
response.raise_for_status()
print(response.json)