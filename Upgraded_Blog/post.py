import requests

posts_url = 'https://api.npoint.io/8440265fff298c576c0f'


class Post:

    def __init__(self, post_id: int):
        response = requests.get(url=posts_url)
        response.raise_for_status()

        post_info = response.json()

        self.id = post_id
        self.title = post_info[self.id - 1]['title']
        self.subtitle = post_info[self.id - 1]['subtitle']
        self.body = post_info[self.id - 1]['body']
        self.author = post_info[self.id-1]['author']
        self.date = post_info[self.id - 1]['date']
