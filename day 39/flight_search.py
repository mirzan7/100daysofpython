import requests
from flight_data import FlightData

tequila_webpage_endpoint = 'https://tequila-api.kiwi.com'
tequila_api_key = '='


class FlightSearch:
    def get_destination_code(self, city_name):
        header = {
            "apikey": tequila_api_key
        }
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{tequila_webpage_endpoint}/locations/query", headers=header, params=query)
        result = response.json()["locations"]
        code = result[0]['code']
        return code

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {
            "apikey": tequila_api_key
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        response = requests.get(url=f"{tequila_webpage_endpoint}/v2/search", headers=header, params=query)
        # response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flight found for {destination_city_code}")
            return None
        # pprint(data)

        flight_data = FlightData(
            price=data['price'],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: {flight_data.price}")
        return flight_data
