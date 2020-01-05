import requests
import random


class EhentaiApi:
    def __init__(self, slug):
        post_data = {
            "method": "gdata",
            "gidlist": [
                [
                    int(slug[:-12]),
                    slug[-12:][1:-1]
                ]
            ],
            "namespace": 1
        }
        headers = {
            "Content-type": "application/json",
            "Accept": "text/plain"
        }
        galleryData = requests.post("https://e-hentai.org/api.php", data=json.dumps(post_data), headers=headers)
        galleryData = json.loads(galleryData.content)
        galleryInfo = [galleryData["gmetadata"][0]["category"], galleryData["gmetadata"][0]["title"], [],
                       galleryData["gmetadata"][0]["rating"], galleryData["gmetadata"][0]["filecount"],
                       galleryData["gmetadata"][0]["tags"], 'n/a', [], galleryData["gmetadata"][0]["thumb"]]
        for x in range(len(galleryInfo[5]) - 1):
            if galleryInfo[5][x][:7] == 'artist:':
                galleryInfo[5][x] = galleryInfo[5][x][7:]
                galleryInfo[2].append(galleryInfo[5][x])
            elif galleryInfo[5][x][:7] == 'female:':
                galleryInfo[5][x] = galleryInfo[5][x][7:]
            elif galleryInfo[5][x][:5] == 'male:':
                galleryInfo[5][x] = galleryInfo[5][x][5:]
            elif galleryInfo[5][x][:7] == 'parody:':
                galleryInfo[5][x] = galleryInfo[5][x][7:]
                galleryInfo[6] = galleryInfo[5][x]
            elif galleryInfo[5][x][:10] == 'character:':
                galleryInfo[5][x] = galleryInfo[5][x][10:]
                galleryInfo[7].append(galleryInfo[5][x])
            elif galleryInfo[5][x][:6] == 'group:':
                galleryInfo[5][x] = galleryInfo[5][x][6:]
            elif galleryInfo[5][x][:9] == 'language:':
                galleryInfo[5][x] = galleryInfo[5][x][9:]
        galleryInfo[2] = ', '.join(galleryInfo[2])
        galleryInfo[5] = ', '.join(galleryInfo[5])
        galleryInfo[7] = ', '.join(galleryInfo[7])
        galleryInfo[3] = round(float(galleryInfo[3]))
        galleryInfo[3] = '★' * galleryInfo[3]
        self.type = galleryInfo[0]
        self.name = galleryInfo[1]
        self.author = galleryInfo[2]
        self.rating = galleryInfo[3]
        self.pages = galleryInfo[4]
        self.tags = galleryInfo[5]
        self.parody = galleryInfo[6]
        self.characters = galleryInfo[7]
        self.thumbnail = galleryInfo[8]