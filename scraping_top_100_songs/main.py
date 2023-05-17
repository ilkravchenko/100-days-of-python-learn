import pprint
import spotipy
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'f218be15a72943e1a1ec9ed60567dde8'
CLIENT_SECRET = '814c228a45534913badd9818ad169b98'
REDIRECT_URI = 'http://localhost:3000'

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ") #2002-08-02
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

respone = requests.get(url=URL)
data = respone.text

soup = BeautifulSoup(data, 'html.parser')

songs_title = [song.getText().strip() for song in soup.find_all(name='h3', class_='a-truncate-ellipsis')]


scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]

for song in songs_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

new_playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False,
                                                    description='You can choose any year of top 100 songs')

sp.playlist_add_items(playlist_id=new_playlist['id'], items=song_uris)