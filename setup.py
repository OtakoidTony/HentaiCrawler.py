from setuptools import setup

with open("README.md") as rm:
    long_description = rm.read()

setup(
    name = "HentaiCrawler",
    version = "0.1.0",
    packages = ["HentaiCrawler",],
    license = "MIT",
    author='Rojiku, OtakoidTony, Park Hyun',
    url = "https://github.com/OtakoidTony/HentaiCrawler.py",
    python_requires = ">=3.5",
    platforms = ['Windows', "Linux", "OSX"],
    description = "Hentai Website Crawling Library",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = "Hentai Crawling Hitomi",
    install_requires = [
        "requests",
        "BeautifulSoup4",
        "random"
    ]
)
