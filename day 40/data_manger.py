import requests
from pprint import pprint

sheety_website_endpoint = "https://api.sheety.co/ee4d2cb035b19a9b20407f70f110a318/flightDeals/sheet1"

class DataManager :
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheety_website_endpoint)
        result = response.json()
        self.destination_data = result['sheet1']
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_website_endpoint}/{city['id']}", json=new_data)
            print(response.text)
