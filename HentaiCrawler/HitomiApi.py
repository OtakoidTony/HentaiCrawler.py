import requests
from bs4 import BeautifulSoup

class Hitomi:
    def getInfo(self, number):
        input_url = 'https://hitomi.la/galleries/' + number + ".html"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        res = requests.get(input_url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        link = soup.find('a')
        input_url = link.get('href')

        res = requests.get(input_url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')

        gallery_info_ul = soup.find_all('ul', attrs={'class': "tags"})
        print(gallery_info_ul)
        character_ul = gallery_info_ul[0]
        print(character_ul)
        character_li = character_ul.find_all('li')
        tags_ul = gallery_info_ul[1]
        tags_li = tags_ul.find_all('li')
        artist_ul = soup.find("ul", attrs={'class': "comma-list"})
        artist_li = artist_ul.find_all('li')
        cover_div = soup.find('div', attrs={'class': "cover"})
        cover_img = cover_div.find('img')
        cover = "https:" + cover_img.get('src')

        type = soup.find('title').text.split('- Read Online - hentai ')[1].split(' | Hitomi.la')[0]

        if type == 'manga':
            title_div = soup.find('div', attrs={'class': "gallery manga-gallery"})
            title = title_div.find('a', attrs={'href': "/reader/" + number + ".html"}).text
        if type == 'doujinshi':
            title_div = soup.find('div', attrs={'class': "gallery dj-gallery"})
            title = title_div.find('a', attrs={'href': "/reader/" + number + ".html"}).text
        if type == 'artistcg':
            title_div = soup.find('div', attrs={'class': "gallery acg-gallery"})
            title = title_div.find('a', attrs={'href': "/reader/" + number + ".html"}).text
        artist = []
        for i in artist_li:
            artist.append(i.text)
        tags = []
        for i in tags_li:
            tags.append(i.text)
        character = []
        for i in character_li:
            character.append(i.text)

        self.number = number
        self.tags = tags
        self.title = title
        self.character = character
        self.cover = cover
        self.artist = artist
        self.type = type

    def searchTag(self, tagPage):
        if tagPage in ['123', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x','y','z']:
            input_url = "https://hitomi.la/alltags-" + tagPage + ".html"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
            res = requests.get(input_url, headers=headers)
            soup = BeautifulSoup(res.content, 'html.parser')
            tags = soup.find("ul", attrs={'class': "posts"})
            a = tags.find_all('a')
            tags = tags.find_all('li')
            tagsReturn = []
            hrefReturn = []
            for i in tags:
                tagsReturn.append(i.text)
            for i in a:
                hrefReturn.append("https://hitomi.la"+i.get('href'))
            print(tagsReturn)
            print(hrefReturn)

            self.tags = tagsReturn
            self.href = hrefReturn