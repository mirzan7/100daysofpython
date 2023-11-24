from flight_search import FlightSearch
from data_manger import DataManager
from datetime import datetime, timedelta
from pprint import pprint
from notification_manger import NotificationManager
from user_interaction import UserInteraction




departure_location = "MAA"
data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager
pprint(sheet_data)

# checking if all the IATA code are present, if not fill it
if sheet_data[0]["iataCode"] == "":
    print("hi")
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row['city'])
    print(sheet_data)
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

# # checking for flights
tomorrow = datetime.now()+timedelta(days=1)
six_month_from_tomorrow = datetime.now() + timedelta(days=(6*30))

userinteraction = UserInteraction()
userinteraction.get_user_data()

for destination_code in destinations:
    flight = flight_search.check_flight(departure_location, destination_code, tomorrow, six_month_from_tomorrow)
    if flight is None:
        continue
    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.get_customer_email()
        emails = [row["email"]for row in users]
        names = [row["firstname"] for row in users]
        message_text = (f"low price alert! only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport}to"
                   f" {flight.destination_city}-{flight.destination_airport}, from{flight.out_date} to {flight.return_date}")
        if flight.stop_overs > 0:
            message_text += f"\nflight has {flight.stop_overs} stop over, via{flight.via_city}."
        link = ""
        notification_manager.send_email(emails, message_text, link)



