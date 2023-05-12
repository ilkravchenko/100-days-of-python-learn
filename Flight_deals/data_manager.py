from pprint import pprint
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.URL = 'https://api.sheety.co/afc5d065101c9878aa70979681937148/flightDeals/prices'

        self.destination_data = {}

    def get_all_data(self):
        response = requests.get(url=self.URL)
        data = response.json()
        self.destination_data = data['prices']

        return (self.destination_data)

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.URL}/{city['id']}",
                json=new_data
            )
            print(response.text)
