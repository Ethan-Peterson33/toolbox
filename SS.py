import bs4
import urllib
from bs4 import BeautifulSoup as soup


class SexyScraper:

    def __init__(self, url):
        self.url = url
        self.parser = 'html5lib'
        self.html = None

    def get_html(self):
        req = urllib.request.Request(self.url, headers={'User-Agent': 'Mozilla/5.0'}) 
#the addition of the headers allows you to scrap websites that dont allow it 
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        response.close()
        self.html = the_page
    
    def parsed(self):
        self.parsed = soup(self.html, self.parser)

    def find(self,tag):
        self.find_list = self.parsed.find_all(tag)
        self.find_item = self.parsed.find(tag)

