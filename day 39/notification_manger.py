import requests
from flight_data import FlightData

sms_endpoint = ""
sms_api_key = ""
flight_data = FlightData
class NotificationManager:

    def __init__(self, lowest_price):
        self.lowest_price = lowest_price

    def check_if_price_is_lower(self):
        if self.lowest_price < flight_data.return_price():
            print("send sms")


