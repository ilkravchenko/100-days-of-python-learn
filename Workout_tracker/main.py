# import os
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

# TASK 1 NUTRITIONIX API
APP_ID = '8d9c60ca'
API_KEY = 'fa854eabf4a4d690cad74c705b0015f9'

HEADERS = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0'
}

URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'

GENDER = 'male'
WEIGHT_KG = 62
HEIGHT_CM = 185
AGE = 21

user_excercises = input("Tell me which excercises you did: ")
excercise_input = {
    'query': user_excercises,
    'gender': GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

responce = requests.post(url=URL, json=excercise_input, headers=HEADERS)
data = responce.json()
# print(data)
# data = {'exercises': [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 20.01, 'met': 9.8, 'nf_calories': 202.63, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}, {'tag_id': 100, 'user_input': 'walked', 'duration_min': 24.85, 'met': 3.5, 'nf_calories': 89.87, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/100_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 17190, 'name': 'walking', 'description': None, 'benefits': None}]}
excercises = [ex for key, value in data.items() for ex in value]
print(excercises)

# TASK 2 SHEETY API

SHEETY_URL = 'https://api.sheety.co/afc5d065101c9878aa70979681937148/workoutTracking/workouts'
USERNAME = 'illia'
PASSWORD = 'Zwer.190'
today = datetime.now()

for exerc in excercises:
    date = today.strftime('%d/%m/%Y')
    time = today.strftime('%X')
    excercise = exerc['name'].title()
    duration = exerc['duration_min']
    calories = exerc['nf_calories']

    new_row = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': excercise,
            'duration': duration,
            'calories': calories,
        }
    }

    basic = HTTPBasicAuth(username=USERNAME, password=PASSWORD)

    sheety_response = requests.post(url=SHEETY_URL, json=new_row, auth=basic)
    print(sheety_response.text)
