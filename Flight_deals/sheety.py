import requests


class SheetyManager:

    def __init__(self):
        self.URL = "https://api.sheety.co/afc5d065101c9878aa70979681937148/flightDeals/users"

        self.all_users = {}

    def get_all_users(self):
        response = requests.get(url=self.URL)
        data = response.json()

        self.all_users = data['users']

        return self.all_users

    def add_user(self, first_name, second_name, email):
        new_user = {
            'user': {
                'firstName': first_name,
                'lastName': second_name,
                'email': email,
            }
        }

        response = requests.post(url=self.URL, json=new_user)
        response.raise_for_status()
        print(response.text)