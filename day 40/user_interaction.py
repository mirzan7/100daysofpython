import requests

SHEETY_WEBSITE_ENDPOINT = "https://api.sheety.co/ee4d2cb035b19a9b20407f70f110a318/flightDeals/users/"

class UserInteraction:

    def __init__(self):
        print("welcome to mizan's flight club."
              "we find the best flight deals and email you")
        self.first_name = ""
        self.last_name = ""
        self.email = ""


    def get_user_data(self):
        self.first_name = input("Enter you first name  :")
        self.last_name = input("Enter your last name  :")
        self.email = input("Enter your email  :")
        user_data = {
            "user": {
                "firstname": self.first_name,
                "lastname": self.last_name,
                "email": self.email
            }
        }
        response = requests.post(url=SHEETY_WEBSITE_ENDPOINT, json=user_data)
        print(response.text)
        response.raise_for_status()

