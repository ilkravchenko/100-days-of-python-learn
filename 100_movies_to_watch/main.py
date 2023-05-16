import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

movies_title = [title.getText() for title in soup.find_all(name='h3', class_='title')]
movies_title = movies_title[::-1]

with open('movies.txt', 'w', encoding='utf-8') as file:
    for film in movies_title:
        file.write(f"{film}\n")
