from flight_search import FlightSearch
from data_manger import DataManager
from datetime import datetime, timedelta
from pprint import pprint
from notification_manger import NotificationManager

departure_location = "LON"
data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

# checking if all the IATA code are present, if not fill it
if sheet_data[0]["iataCode"] == "":
    print("hi")
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row['city'])
    print(sheet_data)
    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()

# # checking for flights
tomorrow = datetime.now()+timedelta(days=1)
six_month_from_tomorrow = datetime.now() + timedelta(days=(6*30))

for row in sheet_data:
    lowest_price = flight_search.check_flight(departure_location, row["iataCode"], tomorrow, six_month_from_tomorrow)
    if flight_data.price < destination["lowestPrice"]:

