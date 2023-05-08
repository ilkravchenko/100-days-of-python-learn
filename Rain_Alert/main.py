import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https' : os.environ['https_proxy']}

API_KEY = "edaa3631968f9462b7fb45430c89f83e"
URL = "https://api.openweathermap.org/data/2.5/onecall"

twilio_sid = "ACb91fa80f036c5ee2e25b60ced5b70871"
token = '8ceaf4fac0e3bc717c3330063aec5302'
account_sid = os.environ[twilio_sid]
auth_token = os.environ[token]

parameters = {
    'lat': 50.447731,
    'lon': 30.542721,
    'exclude': "current,minutely,daily",
    'appid': API_KEY
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

weather_data = response.json()

# result = ''
# for i in range(0,13):
#     if int(weather_data['hourly'][i]['weather'][0]['id']) < 700:
#         result = "Bring an umbrella!"
#     else:
#         result = "Good Weather today!"
#
# print(result)

weather_slice = weather_data['hourly'][:12]
result = False

for hour_data in weather_slice:
    condition_code = hour_data[['weather'][0]['id']]

    if int(condition_code) < 700:
        result = True

if result:
    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+12543234708',
        to='+380995327348'
    )

    print(message.status)