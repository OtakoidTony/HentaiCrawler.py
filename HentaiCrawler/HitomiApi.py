import requests
from bs4 import BeautifulSoup

class Hitomi:
    def __init__(self, number):
        input_url = 'https://hitomi.la/galleries/' + number + ".html"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        res = requests.get(input_url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        print(soup)
        link = soup.find('a')
        input_url = link.get('href')

        res = requests.get(input_url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        
        gallery_info_ul = soup.find_all('ul', attrs={'class': "tags"})
        character_ul = gallery_info_ul[0]
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
