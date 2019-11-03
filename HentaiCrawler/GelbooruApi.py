import requests
from bs4 import BeautifulSoup
import random

class Gelbooru:
    def __init__(self, tags):
        # https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tag=loli
        tags = tags.replace(' ', '+')
        url = ("https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&tags=" + tags+"&api_key=anonymous&user_id=9455")
        res = requests.get(url)
        res = res.json()
        data = random.choice(res)

        self.source = data['source']
        self.directory = data['directory']
        self.hash = data['hash']
        self.height = data['height']
        self.id = data['id']
        self.image = data['image']
        self.change = data['change']
        self.owner = data['owner']
        self.parent_id = data['parent_id']
        self.rating = data['rating']
        self.sample = data['sample']
        self.sample_height = data['sample_height']
        self.sample_width = data['sample_width']
        self.score = data['score']
        self.tags = data['tags']
        self.width = data['width']
        self.file_url = data['file_url']
        self.created_at = data['created_at']

        self.image_size = str(data['width']) + ' × ' + str(data['height'])
        self.sample_size = str(data['sample_width']) + ' × ' + str(data['sample_height'])