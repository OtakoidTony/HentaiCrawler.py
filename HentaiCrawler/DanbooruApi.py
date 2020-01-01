import requests
import random

class Danbooru:
    def __init__(self, tags):
        url = ("https://danbooru.donmai.us/posts.json?page=" + str(random.randrange(1, 5)) + "&limit=100&tags=" + tags)
        res = requests.get(url)
        res = res.json()
        data = random.choice(res)
        
        tags = data['tag_string']
        tags = tags.replace("/\\/\\/\\ ", "")

        self.id = data['id']
        self.created_at = data['created_at']
        self.source = data['source']
        
        self.image_width = data['image_width']
        self.image_height = data['image_height']
        self.image_size = str(data['image_width'])+' × '+str(data['image_height'])
        
        self.file_ext   = data['file_ext']
        self.updated_at = data['updated_at']
        
        self.tags       = tags
        self.pixiv_id   = data['pixiv_id']
        self.artist     = data['tag_string_artist']
        self.character  = data['tag_string_character']
        self.copyright  = data['tag_string_copyright']
        
        
        # ================[ Image Files ]================
        self.file       = data['file_url']
        self.large      = data['large_file_url']
        self.preview    = data['preview_file_url']
