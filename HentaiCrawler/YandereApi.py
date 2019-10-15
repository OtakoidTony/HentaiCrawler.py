import requests
from bs4 import BeautifulSoup
import random

class YandereApi:
    def __init__(self, tags):
        url = ("https://yande.re/post.json?limit=100&page=" + str(random.randrange(1, 5)) + "&tags=" + tags)
        res = requests.get(url)
        res = res.json()
        data = random.choice(res)

        self.id = data['id']
        self.tags = data['tags']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator_id = data['creator_id']
        self.approver_id = data['approver_id']
        self.author = data['author']
        self.change = data['change']
        self.source = data['source']
        self.file = data['file_url']
        self.preview = data['preview_url']
        self.sample = data['sample_url']
        self.jpeg = data['jpeg_url']
