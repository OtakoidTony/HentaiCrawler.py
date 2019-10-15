class Htv:
    def __init__(self, title):
        title = title.replace(' ', '-')
        input_url = 'https://hanime.tv/videos/hentai/' + title
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        res = requests.get(input_url, headers=headers)
        soup = BeautifulSoup(res.content, 'html.parser')
        cover_div = soup.find('div', attrs={'class': "hvpi-cover-container"})
        cover_img = cover_div.find('img')
        cover = cover_img.get('src')
        title = soup.find('h1', attrs={'class': 'tv-title'}).text
        brand = soup.find('a', attrs={'class': "hvpimbc-text"}).text
        desc = soup.find('div', attrs={'class': 'mt-3 mb-0 hvpist-description'}).text
        desc = desc.replace('\n', '')
        soup = soup.find('div', attrs={'class': "hvpi-summary"})
        tags_a = soup.find_all('a')
        tags = []
        for i in tags_a:
            tags.append(i.text)

        self.title = title
        self.desc = desc
        self.tags = tags
        self.brand = brand
        self.cover = cover
