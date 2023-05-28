import requests

posts_url = 'https://api.npoint.io/c790b4d5cab58020d391'


class Post:

    def __init__(self, post_id: int):
        response = requests.get(url=posts_url)
        response.raise_for_status()

        post_info = response.json()

        self.id = post_id
        self.title = post_info[self.id - 1]['title']
        self.subtitle = post_info[self.id - 1]['subtitle']
        self.body = post_info[self.id - 1]['body']
