import requests
from datetime import datetime

GRAPH = 'graph1'
USERNAME = 'lliakrav'
TOKEN = "lsjdfh9234dj92567fghdkjzx73kljh2089"
headers = {
    'X-USER-TOKEN' : TOKEN
}

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',
}
######### Create user ###########
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id' : GRAPH,
    'name' : 'Programing Graph',
    'unit' : 'Courses',
    'type' : 'int',
    'color' : 'momiji',
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}'

today = datetime.now()
# print(today.strftime('%Y%m%d'))

pixel_config = {
    'date' : today.strftime('%Y%m%d'),
    'quantity' : input("How many Courses you'he done today?: "),
}

# response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

date = datetime(year=2023, month=5, day=10).strftime('%Y%m%d')
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"

pixel_update_config = {
    'quantity' : '2'
}

# response = requests.put(url=update_pixel_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
